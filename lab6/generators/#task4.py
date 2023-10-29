#task4 gen

# square from a to b

def square(n1, n2):
    for i in range(n1, n2+1):
        yield i**2
        

a=int(input("Enter 1st value: "))
b=int(input("Enter 2nd value: "))

for i in square(a, b):
    print(i, end=' ')

