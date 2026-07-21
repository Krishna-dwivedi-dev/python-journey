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


# ============================================================
# Day 9 - Bonus Project: Employee Salary Manager
# ============================================================

# -----------------------------------------------------------
# Q1: Save employees list to a file
# -----------------------------------------------------------
def save_employees(employees):
    f = open("employees.txt", "w")
    for employee in employees:
        f.write(f"{employee['Name']}:{employee['Salary']}\n")
    f.close()


# -----------------------------------------------------------
# Q2: Load employees from file and return list of dicts
# -----------------------------------------------------------
def load_employees():
    f = open("employees.txt", "r")
    data = f.read()
    lines = data.split("\n")
    employee_list = []
    for line in lines:
        if line == "":
            continue
        parts = line.split(":")
        employee = {"Name": parts[0], "Salary": int(parts[1])}
        employee_list.append(employee)
    f.close()
    return employee_list


# -----------------------------------------------------------
# Q3: Find and display the highest paid employee
# -----------------------------------------------------------
def highest_paid(employees):
    highest = employees[0]
    for employee in employees:
        if employee['Salary'] > highest['Salary']:
            highest = employee
    print(f"Highest Salary: {highest['Name']} - {highest['Salary']}")


# -----------------------------------------------------------
# Testing all three functions
# -----------------------------------------------------------
employees = [
    {"Name": "krishna", "Salary": 1550000},
    {"Name": "Manisha", "Salary": 2070000}
]

save_employees(employees)
print("Employees saved successfully!")

result = load_employees()
print("Loaded employees:", result)

highest_paid(result)