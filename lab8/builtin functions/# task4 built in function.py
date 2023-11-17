# task4 built in function
import math 
import time

def squareroot(num, ms):
    time.sleep(ms/1000.0)
    return float(math.sqrt(num))

number=int(input())
milisec=int(input())
res=squareroot(number, milisec)
print(f"Square root of {number} after {milisec} miliseconds is {res}")

