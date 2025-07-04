from flask import Blueprint, request, jsonify, session
from app import USERS, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    user = USERS.get(username)
    if user and user['password'] == password:
        session['user'] = username
        session['role'] = user['role']
        return jsonify({'message': 'Login successful', 'role': user['role']})
    return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required()
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'}) 