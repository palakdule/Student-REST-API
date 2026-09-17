from flask import Flask, request
import sqlite3

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("students.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return "Student REST API is running!"


@app.route("/students")
def get_students():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return [dict(student) for student in students]


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or "name" not in data or "course" not in data:
        return {"message": "Name and course are required!"}, 400

    name = data["name"]
    course = data["course"]

    if not name.strip() or not course.strip():
        return {"message": "Name and course cannot be empty!"}, 400

    connection = sqlite3.connect("students.db")

    connection.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        (name, course)
    )

    connection.commit()
    connection.close()

    return {"message": "Student added successfully!"}


@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    if not data or "name" not in data or "course" not in data:
        return {"message": "Name and course are required!"}, 400

    name = data["name"]
    course = data["course"]

    if not name.strip() or not course.strip():
        return {"message": "Name and course cannot be empty!"}, 400

    connection = sqlite3.connect("students.db")

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if student is None:
        connection.close()
        return {"message": "Student not found!"}, 404

    connection.execute(
        "UPDATE students SET name = ?, course = ? WHERE id = ?",
        (name, course, id)
    )

    connection.commit()
    connection.close()

    return {"message": "Student updated successfully!"}


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    connection = sqlite3.connect("students.db")

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if student is None:
        connection.close()
        return {"message": "Student not found!"}, 404

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    return {"message": "Student deleted successfully!"}


@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    connection.close()

    if student is None:
        return {"message": "Student not found!"}, 404

    return dict(student)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)