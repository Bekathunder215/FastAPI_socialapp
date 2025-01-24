# FastAPI Social App

This project is a social media application built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Features

- **User Authentication**: Secure user registration and login functionality.
- **Post Creation**: Users can create, read, update, and delete posts.
- **Database Integration**: Utilizes SQLAlchemy for ORM and PostgreSQL as the database backend.
- **Data Validation**: Pydantic models for data validation and serialization.
- **Password Hashing**: Implements password hashing for secure storage.
- **Environment Configuration**: Uses environment variables for configuration management.
- **Database Versioning**: Uses Alembic for managing database schema migrations efficiently.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Relational database system.
- **Pydantic**: Data validation and settings management.
- **Passlib**: Password hashing library.
- **Python-Decouple**: For reading environment variables.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Alembic**: Database migration tool for handling schema versioning and upgrades/downgrades.

## Project Structure


- `main.py`: Entry point of the application.
- `models.py`: Contains SQLAlchemy models.
- `schemas.py`: Contains Pydantic models (schemas).
- `database.py`: Database connection and session management.
- `crud.py`: Functions for database operations.
- `auth.py`: Authentication-related functions.
- `config.py`: Configuration settings.
- `migrations/`: Contains Alembic configurations and migration scripts.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- **Python 3.7+**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/).
- **PostgreSQL**: Install PostgreSQL and ensure it's running. You can download it from [postgresql.org](https://www.postgresql.org/).

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Bekathunder215/FastAPI_socialapp.git
   cd FastAPI_socialapp

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt

4. **Configure Environment Variables**:

    Create a `.env` file in the root directory with the following content
    ```env
    DATABASE_URL=postgresql://username:password@localhost/dbname
    SECRET_KEY=your_secret_key
    ```
    Replace `username`, `password`, `localhost`, and `dbname` with your PostgreSQL credentials and desired database name. Replace `your_secret_key` with a secure secret key for JWT.

5. **Apply Database Migrations**:
   
    Ensure your PostgreSQL server is running and the database specified in `DATABASE_URL` exists.
    ```bash
    alembic upgrade head
    ```

    To create a new migration after modifying models, use:
    ```bash
    alembic revision --autogenerate -m "Description of changes"
    ```
    

### Running the Application


Start the FastAPI application using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The application will be accessible at `http://127.0.0.1:8000`.

### API Documentation

FastAPI provides interactive API documentation. Once the application is running, you can access it at:

Swagger UI: `http://127.0.0.1:8000/docs`

ReDoc: `http://127.0.0.1:8000/redoc`

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
