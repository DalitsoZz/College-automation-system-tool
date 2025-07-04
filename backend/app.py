from flask import Flask, request, jsonify, send_file, session, redirect
import os
from werkzeug.utils import secure_filename
from doc_extractor import DocumentExtractor  # Your unified extractor
from flask_cors import CORS  # Import CORS
import psycopg2
import io
import requests
import time
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

load_dotenv()

def get_env_or_error(var, varname):
    if var is None:
        raise RuntimeError(f"Missing required environment variable: {varname}")
    return var

def get_db_connection():
    dbname = get_env_or_error(os.environ.get('DB_NAME'), 'DB_NAME')
    user = get_env_or_error(os.environ.get('DB_USER'), 'DB_USER')
    password = get_env_or_error(os.environ.get('DB_PASSWORD'), 'DB_PASSWORD')
    host = get_env_or_error(os.environ.get('DB_HOST'), 'DB_HOST')
    port = get_env_or_error(os.environ.get('DB_PORT'), 'DB_PORT')
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=int(port)
    )

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_secret')

# Simple in-memory user store for demonstration
USERS = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'faculty': {'password': 'facultypass', 'role': 'faculty'},
    'student': {'password': 'studentpass', 'role': 'student'},
}

def login_required(role=None):
    def decorator(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user' not in session:
                return jsonify({'error': 'Authentication required'}), 401
            if role and session.get('role') != role:
                return jsonify({'error': 'Unauthorized'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def is_allowed_file(filename, allowed_exts):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts

def validate_json_fields(data, required_fields):
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, None

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    valid, error = validate_json_fields(data, ['username', 'password'])
    if not valid:
        return jsonify({'error': error}), 400
    username = data.get('username')
    password = data.get('password')
    user = USERS.get(username)
    if user and user['password'] == password:
        session['user'] = username
        session['role'] = user['role']
        return jsonify({'message': 'Login successful', 'role': user['role']})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'})

@app.route('/upload', methods=['POST'])
@login_required()
def upload_file():
    file = request.files.get('file')
    if not file or file.filename is None or file.filename == '':
        return jsonify({"error": "No file provided"}), 400
    if not is_allowed_file(file.filename, {'pdf', 'docx'}):
        return jsonify({"error": "File type not allowed. Only PDF and DOCX accepted."}), 400
    if file.content_length and file.content_length > 10 * 1024 * 1024:
        return jsonify({"error": "File too large. Max 10MB allowed."}), 400
    filename = secure_filename(str(file.filename))
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    try:
        extractor = DocumentExtractor(file_path)
        extracted_text = extractor.extract_text()
        extractor.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"text": extracted_text})

@app.route('/assignments', methods=['GET'])
@login_required()
def get_assignments():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, student_id, title, file_ext, mime_type, file_size_bytes FROM assignments")
        rows = cur.fetchall()
        assignments = [
            {
                'id': row[0],
                'student_id': row[1],
                'title': row[2],
                'file_ext': row[3],
                'mime_type': row[4],
                'file_size_bytes': row[5]
            }
            for row in rows
        ]
        cur.close()
        conn.close()
        return jsonify({'assignments': assignments})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/assignment/<int:assignment_id>/file', methods=['GET'])
@login_required()
def get_assignment_file(assignment_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT file_data, mime_type, title, file_ext FROM assignments WHERE id = %s", (assignment_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            return jsonify({'error': 'Assignment not found'}), 404
        file_data, mime_type, title, file_ext = row
        return send_file(
            io.BytesIO(file_data),
            mimetype=mime_type,
            as_attachment=False,
            download_name=f'{title}.{file_ext}'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/scan_assignments', methods=['POST'])
@login_required(role='admin')
def scan_assignments():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, file_ext, mime_type, file_data FROM assignments")
        rows = cur.fetchall()
        results = {}
        for row in rows:
            assignment_id, title, file_ext, mime_type, file_data = row
            temp_path = f"temp_{assignment_id}.{file_ext}"
            with open(temp_path, 'wb') as f:
                f.write(file_data)
            try:
                extractor = DocumentExtractor(temp_path)
                text = extractor.extract_text()
                extractor.close()
            except Exception as e:
                text = ''
            os.remove(temp_path)
            try:
                api_resp = requests.post(
                    'https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/',
                    json={'text': text},
                    headers={
                        'x-rapidapi-key': os.environ.get('RAPIDAPI_KEY'),
                        'x-rapidapi-host': 'ai-content-detector-ai-gpt.p.rapidapi.com',
                        'Content-Type': 'application/json',
                    }
                )
                scan_result = api_resp.json()
            except Exception as e:
                scan_result = {'error': str(e)}
            results[str(assignment_id)] = scan_result
        cur.close()
        conn.close()
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/scan_assignment/<int:assignment_id>', methods=['POST'])
@login_required(role='admin')
def scan_assignment(assignment_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT title, file_ext, mime_type, file_data FROM assignments WHERE id = %s", (assignment_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            return jsonify({'error': 'Assignment not found'}), 404
        title, file_ext, mime_type, file_data = row
        temp_path = f"temp_{assignment_id}.{file_ext}"
        with open(temp_path, 'wb') as f:
            f.write(file_data)
        try:
            extractor = DocumentExtractor(temp_path)
            text = extractor.extract_text()
            extractor.close()
        except Exception as e:
            text = ''
        os.remove(temp_path)
        try:
            api_resp = requests.post(
                'https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/',
                json={'text': text},
                headers={
                    'x-rapidapi-key': os.environ.get('RAPIDAPI_KEY'),
                    'x-rapidapi-host': 'ai-content-detector-ai-gpt.p.rapidapi.com',
                    'Content-Type': 'application/json',
                }
            )
            scan_result = api_resp.json()
        except Exception as e:
            scan_result = {'error': str(e)}
        return jsonify({'result': scan_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/extract_text', methods=['POST'])
@login_required()
def extract_text():
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400
    file = request.files['pdf']
    if file.filename is None or file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    if not is_allowed_file(file.filename, {'pdf'}):
        return jsonify({"error": "File must be a PDF"}), 400
    if file.content_length and file.content_length > 10 * 1024 * 1024:
        return jsonify({"error": "File too large. Max 10MB allowed."}), 400
    try:
        temp_path = os.path.join(UPLOAD_FOLDER, f"temp_quiz_{secure_filename(str(file.filename))}")
        file.save(temp_path)
        extractor = DocumentExtractor(temp_path)
        extracted_text = extractor.extract_text()
        extractor.close()
        os.remove(temp_path)
        return jsonify({"text": extracted_text})
    except Exception as e:
        return jsonify({"error": f"Failed to extract text: {str(e)}"}), 500

@app.route('/generate_quiz_fallback', methods=['POST'])
@login_required()
def generate_quiz_fallback():
    """Fallback quiz generation when ProProfs API is not available"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        settings = data.get('settings', {})
        
        if not text:
            return jsonify({"error": "No text content provided"}), 400
        
        # Generate simple quiz questions from the text
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 20]
        num_questions = min(int(settings.get('questionCount', 10)), len(sentences))
        
        questions = []
        for i in range(num_questions):
            if i < len(sentences):
                sentence = sentences[i]
                question = {
                    'id': i + 1,
                    'question': f"Based on the content: {sentence[:100]}...",
                    'type': settings.get('type', 'multiple_choice'),
                    'options': [
                        'This statement is correct',
                        'This statement is incorrect', 
                        'This statement is partially correct',
                        'More information is needed'
                    ],
                    'correct_answer': 0,
                    'explanation': 'This question is based on the provided content.'
                }
                questions.append(question)
        
        return jsonify({
            'questions': questions,
            'quiz_id': f"fallback_{int(time.time())}",
            'share_url': None,
            'content': text[:500] + "..." if len(text) > 500 else text
        })
    except Exception as e:
        return jsonify({"error": f"Failed to generate fallback quiz: {str(e)}"}), 500

@app.route('/generate_quiz_gemini', methods=['POST'])
@login_required()
def generate_quiz_gemini():
    data = request.json
    valid, error = validate_json_fields(data, ['text', 'settings'])
    if not valid:
        return jsonify({'error': error}), 400
    text = data.get('text', '')
    settings = data.get('settings', {})
    question_count = settings.get('questionCount', 10)
    difficulty = settings.get('difficulty', 'medium')
    quiz_type = settings.get('type', 'multiple_choice')

    prompt = (
        f"Generate a quiz with {question_count} {difficulty} {quiz_type.replace('_', ' ')} questions "
        f"from the following text:\n\n{text}\n\n"
        "Return the quiz as a JSON array of questions, each with 'question', 'options' (if applicable), and 'correct_answer'."
    )

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    print("[Gemini] Sending request with prompt length:", len(prompt))
    response = requests.post(url, headers=headers, json=payload)
    print("[Gemini] Response status:", response.status_code)
    if response.status_code == 200:
        gemini_data = response.json()
        print("[Gemini] Response JSON:", gemini_data)
        try:
            quiz_json = gemini_data['candidates'][0]['content']['parts'][0]['text']
            import json
            try:
                quiz = json.loads(quiz_json)
                if not isinstance(quiz, list):
                    # If not a list, treat it as a single question
                    quiz = [{
                        'question': quiz_json,
                        'type': quiz_type,
                        'options': [],
                        'correct_answer': ''
                    }]
                return jsonify({"questions": quiz})
            except Exception as e:
                # If the response isn't valid JSON, return as plain text
                print("[Gemini] Could not parse as JSON, returning as text question.")
                quiz = [{
                    'question': quiz_json,
                    'type': quiz_type,
                    'options': [],
                    'correct_answer': ''
                }]
                return jsonify({"questions": quiz, "note": "Returned as plain text because JSON parsing failed.", "parsing_error": str(e)})
        except Exception as e:
            print("[Gemini] Exception during response extraction:", e)
            return jsonify({"error": "Failed to extract quiz from Gemini response", "details": str(e), "raw": gemini_data}), 500
    else:
        print("[Gemini] API error:", response.text)
        return jsonify({"error": "Gemini API error", "details": response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
