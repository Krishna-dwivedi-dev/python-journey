def calculator(a):
    f = (a * 9/5) + 32
    k = a + 273
    return f,k
a = float(input("what is the temprature in celsius "))
result = calculator(a)
print(result)
    