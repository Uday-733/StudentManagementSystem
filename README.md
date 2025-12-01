Student Management System (Python)

A simple and interactive Student Management System built using Python.
This project allows users to add, view, search, update, and delete student records through a text-based menu.

 Features
✔ Add Student

Enter details such as:
ID
Name
Age
Course
Marks

✔ View Students
Displays all stored student records in a clean table format.

✔ Search Student
Search for students based on name.

✔ Update Student
Update any of the following for a given student ID:
Name
Age
Course
Marks

✔ Delete Student
Delete any student record using their ID.

✔ Save & Exit
Ends the program (in-memory storage only).

🧠 Project Structure
Student Management System
│
├── student_management.py   # Main program file
└── README.md               # Project documentation

📂 Code Overview
The project uses:
Lists to store student records

While loops for continuous menu execution

Functions for modular code and cleaner structure

Each student is stored as:

[id, name, age, course, marks]

🖥 Sample Output
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save & Exit
Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Rahul
Enter Student Age: 20
Enter Student Course: Python
Enter Student Marks: 85
Student added successfully!

🛠 Requirements

Python 3.x

No external libraries required

▶️ How to Run

Clone this repository:

git clone https://github.com/yourusername/student-management-system.git


Navigate to the project folder:

cd student-management-system
Run the program:

python student_management.py

📌 Future Enhancements (Optional Ideas)

Add file storage (CSV/JSON)

Add SQLite database support

Build GUI using Tkinter

Convert project into OOP structure

Create web version using Flask/Django

🤝 Contributing

Pull requests are welcome!
If you have ideas to improve this project, feel free to contribute.

📄 License

This project is open-source and available under the MIT License.
