#task3 math
# arae of regular polygon
import math
# from math import cot

n=int(input("Input number of sides: "))
len=int(input("Input the length of a side: "))
area=(n/4)*pow(len,2)/math.tan(math.pi/n)
print("Area of regular polygon: ", round(area))
