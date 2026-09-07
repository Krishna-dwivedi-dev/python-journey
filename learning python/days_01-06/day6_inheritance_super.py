# ===========================================================
# Day 6 - Inheritance Overriding + super()
# ===========================================================

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























