import streamlit as st
from sms import *

st.title("📘 Student Management System")

menu = ["Add Student", "View Students", "Search", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add New Student")
    sid = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.text_input("Age")
    course = st.text_input("Course")
    marks = st.text_input("Marks")

    if st.button("Add"):
        add_student(sid,name,age,course,marks)
        st.success("Student added successfully!")

elif choice == "View Students":
    st.subheader("All Students")
    data = view_students()
    st.table(data)

elif choice == "Search":
    st.subheader("Search Student")
    sname = st.text_input("Enter name to search")
    if st.button("Search"):
        result = search_student(sname)
        if result:
            st.table(result)
        else:
            st.error("Student not found!")

elif choice == "Update":
    st.subheader("Update Student Details")
    sid = st.text_input("Student ID")
    field = st.selectbox("Field to update", ["name","age","course","marks"])
    value = st.text_input("New Value")

    if st.button("Update"):
        if update_student(sid,field,value):
            st.success("Student updated successfully!")
        else:
            st.error("Invalid ID")

elif choice == "Delete":
    st.subheader("Delete Student")
    sid = st.text_input("Enter Student ID")

    if st.button("Delete"):
        if delete_student(sid):
            st.success("Student deleted successfully!")
        else:
            st.error("Invalid ID")