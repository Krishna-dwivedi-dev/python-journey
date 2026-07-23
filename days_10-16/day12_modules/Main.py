# -----------------------------------------------------------
# main.py
# Brings together the Student class and file-handling utilities.
# Part of Day 12: Modules and Packages
# -----------------------------------------------------------

from student import Student
from fileutils import save_students, load_student

# -----------------------------------------------------------
# Quick test of the Student class (imported from student.py)
# -----------------------------------------------------------
student1 = Student("Manisha Dwivedi", 87)
print(student1.get_name())
print(student1.get_marks())
student1.set_marks(99)
print(student1.get_marks())

# -----------------------------------------------------------
# Create students, save them, load them back
# (save_students and load_student are imported from fileutils.py)
# -----------------------------------------------------------
students = [
    {"Name": "Rakesh", "Marks": 77},
    {"Name": "Vikas", "Marks": 86},
    {"Name": "Akansha", "Marks": 99}
]

save_students(students)
print("Students saved successfully!")

result = load_student()

# -----------------------------------------------------------
# Calculate and print the class average
# -----------------------------------------------------------
total_marks = 0
for student in result:
    total_marks = total_marks + student['Marks']

average = total_marks / len(result)
print(f"Class average: {average}")
print(f"Loaded students: {result}")
   