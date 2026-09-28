students = []


# CREATE
def create_student(name, age, course):
    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student created successfully.")


# READ
def read_students():
    print("\nStudent List")
    print("----------------")

    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


# UPDATE
def update_student(student_id, new_course):
    for student in students:
        if student["id"] == student_id:
            student["course"] = new_course
            print("Student updated successfully.")
            return

    print("Student not found.")


# DELETE
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


# Test CRUD operations

create_student("Muhsin", 23, "Python Full Stack")
create_student("Rahul", 24, "Django")

read_students()

update_student(1, "Python Django")

read_students()

delete_student(2)

read_students()