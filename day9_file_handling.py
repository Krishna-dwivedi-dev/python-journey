# ============================================================
# Day 9 - File Handling: Open, Read, Write, Append
# ============================================================

# -----------------------------------------------------------
# Q1: Save students list to a file
# -----------------------------------------------------------
def save_students(students):
    f = open("students.txt", "w")
    for student in students:
        f.write(f"{student['Name']}:{student['Marks']}\n")
    f.close()

# -----------------------------------------------------------
# Q2: Load students from file and return list of dicts
# -----------------------------------------------------------
def load_student():
    f = open("students.txt", "r")
    data = f.read()
    lines = data.split("\n")
    k = []
    for line in lines:
        if line == "":
            continue
        parts = line.split(":")
        D = {"Name": parts[0], "Marks": int(parts[1])}
        k.append(D)
    f.close()
    return k

# -----------------------------------------------------------
# Testing both functions
# -----------------------------------------------------------
students = [
    {"Name": "Ansh", "Marks": 95},
    {"Name": "Rahul", "Marks": 80}
]

save_students(students)
print("Students saved successfully!")

result = load_student()
print("Loaded students:", result)