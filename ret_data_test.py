from flask import Flask, jsonify     # jsonify = Python list/dict -> JSON response

app = Flask(__name__)                # create app = web server

# Data stored in a Python dictionary  -> actually a LIST of dicts
students = [                         # fake "database" in memory
    {                                # 1 dict = 1 student
        "id": 101,
        "name": "Alice",
        "program": "Computer Programming",
        "gpa": 3.8
    },
    {
        "id": 102,
        "name": "Bob",
        "program": "Software Engineering",
        "gpa": 3.6
    }
]

@app.route("/")
def home():
    return "<h2>try return data!!!!</h2>"

@app.route("/student", methods= ["GET"])  # url /student  and GET only (same as default)
def get_student():
    return jsonify(students)  # return a json NOT html 
                            #   Content-Type = application/json

# JSON keys come back sorted A-Z -> gpa, id, name, program
# /students (with s) -> 404, URL = /student
# POST to /student -> 405

# run with Flask's built-in development server with:
# flask --app base_json.py run