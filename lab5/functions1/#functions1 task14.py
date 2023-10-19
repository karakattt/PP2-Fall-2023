#task14 import functions from above 13 tasks
# for example from functions1 task9, use import math
import math
def volume(r):
    pi=3.14
    vol=4/3*pi*math.pow(r,3)
    return vol
out=volume(int(input()))
print(round(out, 2))
