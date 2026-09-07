# -----------------------------------------------------------
# fileutils.py
# File-handling utilities for saving and loading student data.
# Part of Day 12: Modules and Packages
# -----------------------------------------------------------


def save_students(students):
    """
    Save a list of student dictionaries to students.txt.
    Each line is written in the format: Name:Marks
    """
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student['Name']}:{student['Marks']}\n")


def load_student():
    """
    Read students.txt and return a list of student dictionaries.
    Skips empty lines while parsing.
    """
    with open("students.txt", "r") as f:
        data = f.read()

    lines = data.split("\n")
    students = []

    for line in lines:
        if line == "":
            continue
        parts = line.split(":")
        student = {"Name": parts[0], "Marks": int(parts[1])}
        students.append(student)

    return students


# -----------------------------------------------------------
# Test code — only runs when this file is executed directly,
# not when it's imported by another file (like main.py)
# -----------------------------------------------------------
if __name__ == "__main__":
    students = [
        {"Name": "Ansh", "Marks": 95},
        {"Name": "Rahul", "Marks": 80}
    ]

    save_students(students)
    print("Students saved successfully!")

    result = load_student()
    print("Loaded students:", result)