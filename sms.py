# ===============================
# Student Management System (Backend)
# ===============================

students = []

def add_student(student_id, name, age, course, marks):
    students.append([student_id, name, age, course, marks])
    return True


def view_students():
    return students


def search_student(name):
    result = [s for s in students if s[1] == name]
    return result


def update_student(student_id, field, value):
    for s in students:
        if s[0] == student_id:
            fields = {'name':1,'age':2,'course':3,'marks':4}
            if field in fields:
                s[fields[field]] = value
                return True
    return False


def delete_student(student_id):
    for s in students:
        if s[0] == student_id:
            students.remove(s)
            return True
    return False