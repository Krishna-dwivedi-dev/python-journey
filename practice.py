# variable
"""
G = input("what is your name")
k = (input("what is your age"))
k = k + 1
l = (f"my name is {G} I am {k} year old")
print(l)

i = 6
j = 3.14
k = "krishna"
l = True
print(type(i))
print(type(j))
print(type(k))
print(type(l))
"""
"""
# conditionals
i = int(input("what is your marks"))
if i >= 90:   
        print("Grade A")
elif 90 > i >= 75:
        print("Grade B")
elif 75 > i >= 60:
        print("Grade C")
else:
        print("Fail") 
"""
# loops 
"""
n = int(input("what is the number"))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)

num = int(input("number : "))
while num >= 1:
    print(num)
    num = num - 1
if num == 0:
    print("boomblast")    
"""
# function
"""
def calculator(a,b,operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
a = float(input("what is big number"))
b = float(input("what is small number"))    
result = calculator(a,b,"add")
print(result)
result = calculator(a,b,"subtract")
print(result)
result = calculator(a,b,"multiply")
print(result)
"""
    
    
    



    

    

