# ============================================
# Day 1 - Python Revision
# Topics: Variables, Loops, Conditionals, Functions
# ============================================


# Question 1: Temperature Converter
def temperature_converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = 273.15 + celsius
    return (fahrenheit, kelvin)

celsius = float(input("Enter temperature in Celsius: "))
result = temperature_converter(celsius)
print("Fahrenheit:", result[0])
print("Kelvin:", result[1])


# ============================================
# Question 2: Multiplication Table (1-5)
# ============================================

for i in range(1, 6):
    for j in range(1, 6):
        print(i, "X", j, "=", i*j)


# ============================================
# Question 3: Prime Numbers (1-50)
# ============================================

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 50:")
for j in range(2, 51):
    if is_prime(j):
        print(j)

# ============================================================
# DAY 2 REVISION — Lists, Dictionaries, Strings, File Handling
# ============================================================


# ==========================
# Q1 — Get Topper
# ==========================

student_grade = {
    "krishna": 81,
    "rajesh": 75,
    "kasish": 69,
    "aman": 90,
    "diksha": 79,
}

def get_topper(grades):
    topper = max(grades, key=grades.get)
    return topper

result = get_topper(student_grade)
print("Topper:", result)


# ===========================
# Q2 — Word Frequency
# ===========================

def word_frequence(sentense):
    word = sentense.split()
    frequence = {}
    for w in word:
        if w in frequence:
            frequence[w] = frequence[w] + 1
        else:
            frequence[w] = 1
    return frequence

result = word_frequence("hi how are you and who are you hi how you")
print("Word Frequency:", result)


# ==================================
# Q3 — File Write & Read
# ==================================

f = open("grades.txt", "w")
f.write("krishna: 75")
f.write("\nrahul: 80")
f.write("\nzenith: 55")
f.write("\ndiksha: 74")
f.write("\nbhavna: 69")
f.close()

f = open("grades.txt", "r")
grades = f.read()
lines = grades.split("\n")
print("Students with 70+ marks:")
for line in lines:
    parts = line.split(":")
    name = parts[0]
    marks = int(parts[1])
    if marks > 70:
        print(name, marks)
f.close()
    
