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







