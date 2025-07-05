
College Automation System Tool (C.A.S.T)
  C.A.S.T is a unified digital platform designed to modernize the management and administration of higher education institutions. It aims to streamline institutional workflows, improve academic engagement, and provide a centralized ecosystem for administrators, faculty, and students.
Key Features
  C.A.S.T offers a comprehensive suite of tools to enhance various aspects of college operations:
 > Role-Based User Authentication: Secure login system with access privileges customized for administrators, lecturers, and students, ensuring data security and personalized experiences.
 >AI-Powered Assignment Scanner for Lecturers: Automates the processing of submitted assignments, including content extraction and initial analysis, significantly reducing manual grading effort.
 > Auto Quiz Generator: Leverages AI to automatically generate quizzes directly from uploaded lecture materials and assignment content, facilitating efficient assessment creation.
 > Leave Manager for Administrators: Streamlines the leave application and approval process for staff, providing a centralized system for tracking and managing leave requests.
 > 24/7 Chatbot for Student Support: An intelligent chatbot provides instant answers to student queries, offering round-the-clock support on various topics, from academic information to administrative procedures.
 >Assignment Management: Enables efficient submission, storage, and retrieval of assignments with built-in file validation and metadata handling.
 >Modular Backend Architecture: A clearly separated structure comprising routes, services, and utility modules, allowing for maintainability and scalability as the system evolves.
 > Dedicated Frontend Portals: Clean, responsive user interfaces tailored to the specific needs of each user group, ensuring an intuitive and productive experience.
 >Security Compliance: Implements best practices including the use of environment variables, thorough input validation, and strict access control measures to protect sensitive data.
Technology Stack
  C.A.S.T is built with a robust and modern technology stack to ensure performance, scalability, and maintainability:
Backend
 Programming Language: Python 3
 Framework: Flask
 Database Integration: PostgreSQL via psycopg2
 Environment Management: python-dotenv, dotenv
 File Processing: PyMuPDF (fitz)
 Utilities: Werkzeug, requests, Flask Blueprints
 Authentication: Session-based login system
Frontend
  Core Technologies: HTML5, CSS3, JavaScript (ES6+)
 Framework & Styling: Vue.js, Tailwind CSS
 icons: Font Awesome
  Tooling: Vite (for modern build and development workflows)
Development & Utilities
 .env for environment-specific configuration
 .gitignore to maintain version control hygiene
 TQDM for real-time progress tracking in scripts
Project Structure
The application is modular by design. Core logic is initiated in app.py, with backend functionality organized into distinct components for clarity and maintainability. The frontend integrates seamlessly with the backend to provide a responsive and coherent user experience.
Getting Started
Follow these steps to get C.A.S.T up and running on your local machine:
 Clone the Repository:
   git clone <your-repository-url>
cd <your-repository-name>

 Configure Environment Variables:
   Copy the .env.template file to .env and insert your specific configuration values (e.g., database credentials, API keys).
   cp .env.template .env

 Install Dependencies:
   Backend:
     pip install -r requirements.txt

    Frontend:
     npm install

 Start the Application:
  Backend:
     python app.py

    Frontend:
     npm run dev

 * Access the Platform:
   Navigate to the relevant local development URL in your web browser (e.g., http://localhost:5173 for the frontend).
