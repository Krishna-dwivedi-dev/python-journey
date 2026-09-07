#=================================================================================
# Day 10: Context Managers (with statement)
# Covers: custom context managers (__enter__/__exit__), exception handling
# in __exit__, and rewriting file-handling functions using 'with'.
#=================================================================================

# ---------------------------------------------------------
# Q1 (Warm-up): Counter Context Manager
# ---------------------------------------------------------
class Counter:
    def __init__(self, count):
        self.count = count

    def __enter__(self):
        print("Counting Shuru!")
        return self

    def increment(self):
        self.count = self.count + 1
        print(f"Current Count : {self.count}")

    def __exit__(self, exc_type, exc, tb):
        print(f"Counting Khatam! Final Count: {self.count}")


with Counter(0) as f:
    f.increment()
    f.increment()
    f.increment()


# ---------------------------------------------------------
# Q2 (Warm-up): SafeDivider - Exception Handling in __exit__
# ---------------------------------------------------------
class SafeDivider:
    def __init__(self):
        print("Division starting soon")

    def __enter__(self):
        print("Division Started!")
        return self

    def divide(self, a, b):
        return a / b

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("No Error has Occurred")
        else:
            print(exc_type)
            print(exc)
            print(tb)
        return True  # suppress the exception


with SafeDivider() as sd:
    sd.divide(65000, 100)
    sd.divide(10, 0)


# ---------------------------------------------------------
# Q3 (Roadmap): Rewrite save_students / load_student using 'with'
# ---------------------------------------------------------
students = [
    {"Name": "Ansh", "Marks": 95},
    {"Name": "Rahul", "Marks": 80},
    {"Name": "Krishna", "Marks": 85},
    {"Name": "Manisha", "Marks": 90},
    {"Name": "chetan", "Marks": 50}
]


def save_students(students):
    with open("student.txt", "w") as f:
        for student in students:
            f.write(f"{student['Name']}:{student['Marks']}\n")


def load_student():
    with open("student.txt", "r") as f:
        data = f.read()
    lines = data.split("\n")
    k = []
    for line in lines:
        if line == "":
            continue
        parts = line.split(":")
        d = {"Name": parts[0], "Marks": int(parts[1])}
        k.append(d)
    return k


save_students(students)
print("Students saved successfully!")

result = load_student()
print("Loaded students:", result)


# ---------------------------------------------------------
# Q4 (Roadmap): Class Average, Highest, Lowest
# ---------------------------------------------------------
Total = 0
for student in result:
    Total = Total + student['Marks']
Average = Total / len(result)

Highest = result[0]
for student in result:
    if student['Marks'] > Highest['Marks']:
        Highest = student

Lowest = result[0]
for student in result:
    if student['Marks'] < Lowest['Marks']:
        Lowest = student

print(f"Class Average: {Average} | Highest Marks scored by: {Highest['Name']} | Lowest Marks scored by: {Lowest['Name']}")
