College Automation System Tool (C.A.S.T) is a unified digital platform designed to modernize the management and administration of higher education institutions. It aims to streamline institutional workflows, improve academic engagement, and provide a centralized ecosystem for administrators, faculty, and students.

Key Features
Role-Based User Authentication
Secure login system with access privileges customized for administrators, lecturers, and students.

Assignment Management
Enables efficient submission, storage, and retrieval of assignments with built-in file validation and metadata handling.

AI-Powered Document Processing
Integrates with external APIs to extract content from uploaded documents and automatically generate relevant quizzes and insights.

Modular Backend Architecture
A clearly separated structure comprising routes, services, and utility modules, allowing for maintainability and scalability.

Dedicated Frontend Portals
Clean, responsive user interfaces tailored to the specific needs of each user group.

Security Compliance
Implements best practices including the use of environment variables, thorough input validation, and strict access control measures.

Technology Stack
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

Icons: Font Awesome

Tooling: Vite (for modern build and development workflows)

Development & Utilities
.env for environment-specific configuration

.gitignore to maintain version control hygiene

TQDM for real-time progress tracking in scripts

Project Structure
The application is modular by design. Core logic is initiated in app.py, with backend functionality organized into distinct components. The frontend integrates with the backend seamlessly to provide a responsive and coherent user experience.

Getting Started
Clone the Repository

Configure Environment Variables
Copy the .env template file and insert your configuration values.

Install Dependencies

Backend: pip install -r requirements.txt

Frontend: npm install

Start the Application

Backend: run app.py

Frontend: served via Vite or integrated with Flask

Access the Platform
Navigate to the relevant local development URL (e.g., http://localhost:5173)