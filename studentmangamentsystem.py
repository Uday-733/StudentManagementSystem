# ===============================
# Student Management System
# ===============================

# Data Structure
students = []

# -------------------------------
# 1. Add Student
# -------------------------------
def add_student():
    row = []
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")
    marks = input("Enter Student Marks: ")

    row.append(student_id)
    row.append(name)
    row.append(age)
    row.append(course)
    row.append(marks)

    students.append(row)
    print("Student added successfully!\n")


# -------------------------------
# 2. View Students
# -------------------------------
def view_students():
    print("ID\tName\tAge\tCourse\tMarks")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
    print()


# -------------------------------
# 3. Search Student
# -------------------------------
def search_student():
    search_name = input("Enter the name of the student to search: ")
    found = False

    print("ID\tName\tAge\tCourse\tMarks")
    for student in students:
        if student[1] == search_name:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
            found = True

    if not found:
        print("Student not found.")
    print()


# -------------------------------
# 4. Update Student
# -------------------------------
def update_student():
    update_det = input("Enter the column to update (name/age/course/marks): ").lower()
    update_id = input("Enter Student ID to update: ")

    found = False

    for student in students:
        if student[0] == update_id:
            found = True
            if update_det == 'name':
                student[1] = input("Enter new name: ")
            elif update_det == 'age':
                student[2] = input("Enter new age: ")
            elif update_det == 'course':
                student[3] = input("Enter new course: ")
            elif update_det == 'marks':
                student[4] = input("Enter new marks: ")
            else:
                print("Invalid detail type.")
                return

            print("Student details updated successfully!\n")
            return

    if not found:
        print("Invalid Student ID.\n")


# -------------------------------
# 5. Delete Student
# -------------------------------
def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    found = False

    for student in students:
        if student[0] == delete_id:
            students.remove(student)
            found = True
            print("Student deleted successfully!\n")
            break

    if not found:
        print("Invalid Student ID.\n")


# -------------------------------
# 6. Main Menu
# -------------------------------
def menu():
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save & Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Saving data and exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run Program
menu()
