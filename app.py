import streamlit as st
import os

FILE_NAME = "students.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass

def add_student(name, roll, course):
    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{roll},{course}\n")

def view_students():
    students = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                students.append({"Name": parts[0], "Roll": parts[1], "Course": parts[2]})
    return students

def search_student(roll_no):
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[1] == roll_no:
                return {"Name": parts[0], "Roll": parts[1], "Course": parts[2]}
    return None

def delete_student(roll_no):
    lines = []
    found = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    
    with open(FILE_NAME, "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[1] == roll_no:
                found = True
                continue
            f.write(line)
    return found

st.title("Student Management System")

menu = ["Add Student", "View Students", "Search Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add a New Student")
    name = st.text_input("Name")
    roll = st.text_input("Roll Number")
    course = st.text_input("Course")
    if st.button("Add"):
        if name and roll and course:
            if search_student(roll):
                st.error("Student with this Roll Number already exists!")
            else:
                add_student(name, roll, course)
                st.success(f"Student {name} added successfully!")
        else:
            st.warning("Please fill all the fields.")

elif choice == "View Students":
    st.subheader("Student List")
    students = view_students()
    if students:
        st.table(students)
    else:
        st.info("No records found.")

elif choice == "Search Student":
    st.subheader("Search Student")
    roll = st.text_input("Enter Roll Number to Search")
    if st.button("Search"):
        if roll:
            student = search_student(roll)
            if student:
                st.success("Student Found!")
                st.write(f"**Name:** {student['Name']}")
                st.write(f"**Roll Number:** {student['Roll']}")
                st.write(f"**Course:** {student['Course']}")
            else:
                st.error("Student not found!")
        else:
            st.warning("Please enter a roll number.")

elif choice == "Delete Student":
    st.subheader("Delete Student")
    roll = st.text_input("Enter Roll Number to Delete")
    if st.button("Delete"):
        if roll:
            if delete_student(roll):
                st.success(f"Student with Roll Number {roll} deleted successfully!")
            else:
                st.error("Student not found!")
        else:
            st.warning("Please enter a roll number.")
