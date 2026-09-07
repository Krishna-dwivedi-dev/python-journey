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






















