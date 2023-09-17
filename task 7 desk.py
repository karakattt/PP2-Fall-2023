# task7 find the required number of desks
import math

# c means number of students in each Class
c1=int(input())
c2=int(input())
c3=int(input())

#using math.ceil for rounding up
d1=math.ceil(c1/2)
d2=math.ceil(c2/2)
d3=math.ceil(c3/2)

# finding total desks which need to buy
total=d1+d2+d3

print(total)
