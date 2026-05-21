"""
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
    
# ============================================
# Day 3: Python OOP - Classes, Objects, __init__, self
# Author: Krishna Dwivedi
# Date: April 27, 2026
# ============================================


# ====== Q1: Book Class ======
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"{self.title} by {self.author} - {self.pages} pages")

Book1 = Book("Atomic Habit", "James Clear", 285)
Book2 = Book("Dopamine Detox", "Thibaut Meurisse", 53)
Book3 = Book("Master Your Emotions", "Thibaut Meurisse", 209)
Book1.display()
Book2.display()
Book3.display()


# ====== Q2: Rectangle Class ======
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self, number):
        print(f"Rectangle {number}: {self.length} x {self.breadth}")
        print(f"Area = {self.length * self.breadth} sq. units")
        print(f"Perimeter = {2 * (self.length + self.breadth)} units")

rectangle1 = Rectangle(50, 30)
rectangle2 = Rectangle(25, 40)
rectangle1.display(1)
rectangle2.display(2)


# ====== Q3: Student Class ======
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {sum(self.marks) / 3}/50")

student1 = Student("Krishna", 21, [39, 48, 42])
student2 = Student("Diksha", 20, [45, 43, 38])
student1.display()
student2.display()
"""

# ======== Bonus: Bank Account System ========
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited! New Balance = ₹{self.balance}")
        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn! Remaining Balance = ₹{self.balance}")

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Balance: ₹{self.balance}")

BankAccount1 = BankAccount("Krishna Dwivedi", 1080000)
BankAccount1.display()
BankAccount1.deposit(90500)
BankAccount1.withdraw(650000)
BankAccount1.display()

BankAccount2 = BankAccount("Manisha Dwivedi", 590000)
BankAccount2.display()
BankAccount2.deposit(550000)
BankAccount2.withdraw(385000)
BankAccount2.display()


# ============================================================
# Day 5 - Python OOP: Inheritance
# ============================================================
 
 
# --------------------
# Q1: Animal, Dog, Cat
# --------------------
 
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
 
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
 
class Cat(Animal):
    def __init__(self, name, sound, indoor):
        super().__init__(name, sound)
        self.indoor = indoor
 
dog1 = Dog("Tommy", "woof", "labrador")
cat1 = Cat("Jimmi", "Meaow", True)
dog1.speak()
cat1.speak()
print(f"{dog1.name} is a {dog1.breed} and says {dog1.sound}")
print(f"{cat1.name} is a indoor: [{cat1.indoor}] and says {cat1.sound}")
 
 
# ----------------------
# Q2: Vehicle, Car, Bike
# ----------------------
 
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
 
class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors
 
class Bike(Vehicle):
    def __init__(self, brand, speed, has_sidecar):
        super().__init__(brand, speed)
        self.has_sidecar = has_sidecar
 
car1 = Car("Toyota", 130, 4)
bike1 = Bike("splender", 100, False)
print(f"{car1.brand} car with {car1.num_doors} doors and {car1.speed} speed limit")
print(f"{bike1.brand} bike, has sidecar [{bike1.has_sidecar}], speed: [{bike1.speed}]")
 
 
# --------------------------------
# Q3: Character, Warrior, Mage
# --------------------------------
 
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def check_up(self):
        print(f"{self.name} has health [{self.health}]")
 
class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
 
class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)
        self.spell = spell
 
warrior1 = Warrior("kratos", 100, "Sword")
mage1 = Mage("Gandalf", 80, "Fireball")
warrior1.check_up()
mage1.check_up()
print(f"{warrior1.name} has health [{warrior1.health}] and attacks with {warrior1.weapon}")
print(f"{mage1.name} has health [{mage1.health}] and casts {mage1.spell}")


# ====================================================
# Day 6 - Inheritance Overriding + super()
# =====================================================

# --------------------------------------------------
# Q1 - Inheritance Overriding + super() | Person & Student
# --------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old")

class Student(Person):
    def __init__(self, name, age, student_id):
        self.student_id = student_id
        super().__init__(name, age)
    def introduce(self):
        super().introduce()
        print(f"My student ID is {self.student_id}")

s1 = Student("Krishna Dwivedi", 18, "B256748")
s1.introduce()


# --------------------------------------------------
# Q2 - Inheritance Overriding + super() | RPG Character System
# --------------------------------------------------

class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
    def status(self):
        print(f"[{self.name}], HP: {self.health}, Level: {self.level}")

class Warrior(Character):
    def __init__(self, name, health, level, weapon):
        self.weapon = weapon
        super().__init__(name, health, level)
    def status(self):
        super().status()
        print(f"Weapon: {self.weapon}")

class Mage(Character):
    def __init__(self, name, health, level, spell):
        self.spell = spell
        super().__init__(name, health, level)
    def status(self):
        super().status()
        print(f"Spell: {self.spell}")

Warrior1 = Warrior("Karatos", 100, 10, "Axe")
Mage1 = Mage("Gandalf", 80, 15, "Fireball")
Warrior1.status()
Mage1.status()


# --------------------------------------------------
# Q3 - Inheritance Overriding + super() | Vehicle System
# --------------------------------------------------

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def status(self):
        print(f"Vehicle Brand name Is: {self.brand}, And Speed Limit is: {self.speed}")

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_range):
        self.battery_range = battery_range
        super().__init__(brand, speed)
    def status(self):
        super().status()
        print(f"Battery Range is: {self.battery_range}")

class SportsBike(Vehicle):
    def __init__(self, brand, speed, turbo):
        self.turbo = turbo
        super().__init__(brand, speed)
    def status(self):
        super().status()
        print(f"Turbo Enable: {self.turbo}")

Car1 = ElectricCar("Tesla", 250, "500km")
bike1 = SportsBike("Dugati", 300, True)
Car1.status()
bike1.status()
