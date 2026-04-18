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


    
