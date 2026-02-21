# Full Stack Web App – Authentication & Dashboard
This project is a **full-stack web application** built as part of a *Frontend Developer Intern assignment*.  
It demonstrates secure authentication, protected routes, and CRUD operations using a modern tech stack.
---
## Features
### Authentication
- User Signup & Login
- JWT-based authentication
- Password hashing using bcrypt
- Protected routes (Dashboard accessible only after login)
### Dashboard
- Displays logged-in user profile
- Logout functionality
- Secure access using JWT
### Task Management (CRUD)
- Create tasks (title & description)
- View user-specific tasks
- Delete tasks
- Tasks are scoped to the authenticated user
---
## Tech Stack
### Frontend
- React.js
- React Router DOM
- Axios
- Tailwind CSS
- Vite
### Backend
- FastAPI (Python)
- SQLite (database)
- SQLAlchemy (ORM)
- JWT (authentication)
- Passlib & bcrypt (password hashing)
---
## API Documentation
This project uses FastAPI, which provides automatic interactive API documentation.
Swagger UI is available at:
http://127.0.0.1:8000/docs
All authentication, user, and task CRUD endpoints can be tested directly from the Swagger interface.

## Scalability & Production Considerations
If this application were to be scaled for production, the following improvements would be applied:

- Replace SQLite with PostgreSQL for better concurrency and reliability
- Store JWT secrets and database credentials in environment variables
- Add refresh tokens for improved authentication security
- Deploy frontend and backend as separate services
- Use Nginx as a reverse proxy
- Enable HTTPS and secure CORS policies
- Add pagination and indexing for large task datasets
- Containerize services using Docker for easier deployment