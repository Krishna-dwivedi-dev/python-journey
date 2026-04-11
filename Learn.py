"""
h = float(input("what is the height: "))
b = float(input("what is base: "))
area = 2*(h+b)
print(f"the area of triangle is {area}")

a = 6
b = 3.14
d = "minecraft"
print(type(a))
print(type(b))
print(type(d))

a = 1
b = 105
if a and b >100:
    print("good")
elif a and b >4:
    print("CSK")
else:
    print("bad")

    
num = int(input("what is the num"))
for i in range(1,11):
    print(i*num)

    
n = int(input("number : "))
for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):        # i ko j se divide hota hai?
        if i % j == 0:
            is_prime = False       # break bhi laga sakte ho
    if is_prime:
        print(i)
"""
"""
i = int(input("what is your number"))
while i >= 0:
    print(i)
    i = i-1 
print("boomblast!")
"""
"""
import random
k = random.randint(1,100)
i = int(input("guess the number btween 1 to 100"))
while i != k:
    if i < k:
        print("to low")
    elif i > k:
        print("to high")
    i = int(input("guess again"))
print("correct")

def function(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
n = int(input("what is the number"))
function(n)
"""
