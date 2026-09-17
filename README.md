# Student REST API

A simple RESTful API built using Python, Flask, and SQLite for managing student records.

## Features

- Get all students
- Get a student by ID
- Add a new student
- Update student details
- Delete a student
- Input validation
- Error handling for invalid student IDs
- SQLite database integration
- API testing using Postman

## Technologies Used

- Python
- Flask
- SQLite
- Postman
- VS Code
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/<id>` | Get a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/<id>` | Update student details |
| DELETE | `/students/<id>` | Delete a student |

## Example Request

### Add Student

**POST**

```text
http://127.0.0.1:5000/students
```

Request Body:

```json
{
    "name": "Palak",
    "course": "CSE"
}
```

Response:

```json
{
    "message": "Student added successfully!"
}
```

## Validation

The API checks for:

- Missing name or course
- Empty name or course
- Student ID that does not exist

Example error response:

```json
{
    "message": "Student not found!"
}
```

## Database

The project uses SQLite to store student records.

The database file is:

```text
students.db
```

The database file is excluded from GitHub using `.gitignore`.

## How to Run

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

4. Open:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
Student-REST-API/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── students.db
```

> `students.db` is stored locally and is not uploaded to GitHub.

## Learning Outcomes

Through this project, I learned how to:

- Build REST APIs using Flask
- Handle HTTP methods such as GET, POST, PUT, and DELETE
- Connect a Flask application with SQLite
- Perform CRUD operations
- Validate API input
- Handle HTTP error responses
- Test APIs using Postman
- Manage project dependencies using `requirements.txt`
- Use Git and GitHub for project management

## Future Improvements

- Add authentication and authorization
- Add search and filtering
- Use PostgreSQL for production-level database management
- Add automated API testing
- Deploy the API online

## Author

**Palak Dule**
