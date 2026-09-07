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















