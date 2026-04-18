"""
def function(a):
    fahrenhite = (a * 9/5) + 32
    kelvin = 273.15 + a
    return(fahrenhite,kelvin)
a = float(input("what is the temp in celcius"))
result = function(a)
print(result)

for i in range(1,6):
    for j in range(1,6):
        print(i, "X",j,"=",i*j)
        """
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
for j in range(2,51):
 if is_prime(j):
    print(j)

    
