from flask import Flask, request, jsonify # request  = read data the client send
app = Flask(__name__)

# Our "database" is simply a Python list
students = [                                 # in memory -> restart server = back to these 2
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.6}
]

# ------- READ ALL -------
#@app.route("/students", methods=["GET"])    # long way
@app.get("/students")                        # short way, same thing
def get_students():
    return jsonify(students)                 # whole list -> JSON, 200

# ----- READ ONE --------
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for stu in students:
        if stu["id"] == id:
            return jsonify(stu)
    # return jsonify({"error": "student not found"}), 404
    return "print('not found')", 404  # return <p> not found<p> , 4040


# ------ CREATE (JSON) -----------------
# @app.post("/students")
# def add_student():
#     new_stu = request.get_json()
#     students.append(new_stu)
#     return jsonify(new_stu), 201  # code 201 = Created



# ---------- CREATE (form) - commented out ----------
# @app.route("/students", methods=["POST"])
# using form data in the request body
@app.post("/students")
def add_student():                         # same name as above -> can't have both
    new_student = {
        "id": int(request.form["id"]),     # form data = strings -> int()
        "name": request.form["name"],
        "gpa": float(request.form["gpa"]), # string -> float()
    }
    students.append(new_student)
    return "<p>Student added successfully.</p>", 201   # returns HTML, not JSON

# to test switch to x-www-form ***********


# ----------- UPDATE ---------------
@app.put("/students/<int:id>")
def update_student(id):
    update_data = request.get_json()   # getting new value from body

    for stu in students:
        if stu["id"] == id:
            stu.update(update_data)
            return jsonify(stu)
    return jsonify({"error" : "Student not found"}), 404


# ----------DELETE ------------
@app.delete("/students/<int:id>")
def delete_stu(id):
    for stu in students:
        if stu["id"] == id:
            students.remove(stu)  # remove from ls
            return jsonify({"message": "student deleted"})  # 200
    return jsonify({"error" : "Student not found"}), 404