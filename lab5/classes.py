#classes
# task1 classes
#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class string:
    def __init__(self):
        self.str=""
    def getsrting(self):
        self.str=input()
    
    def printstring(self):
        print(self.str.upper())
s=string()
s.getsrting()
s.printstring()




 

 

# task2 classes
#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# class shape:
#     def __init__(self):
#         self.area=0


# class square(shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length=length
#     def area_(self):
#         return self.length**2

# sq=square(5)
# print(sq.area_())



 

 

#task3 classes
#Define a class named Rectangle which inherits from Shape class from task 2. 
#Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
# class shape:
#     def __init__(self):
#         self.area=0

# class rectangle(shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length=length
#         self.width=width
#     def area_(self):
#         return self.length*self.width

# rc=rectangle(5, 4)
# print(rc.area_())

 

 

 

 

#task4 classes
# class point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y

#     def show(self):
#         print(self.x, self.y)

#     def move(self, a, b):
#         self.x=a
#         self.y=b

#     def distance(self, oth):
#         dx=self.x-oth.x
#         dy=self.y-oth.y
#         dist=(dx**2 + dy**2)**0.5
#         return dist
# p1=point(1,2)
# p2=point(4,6)
 
# p1.show()
# p2.show()

# print(round(p1.distance(p2),3))

 





#task5 classes
# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# class account:
#     def __init__(self, owner, balance=0):
#         self.owner=owner
#         self.balance=balance
    
#     def deposite(self, dep):
#         self.balance+=dep
#         print(f"New balance after deposite: {self.balance}")
#         # print(self.balance)
    
#     def withdraw(self, wd):
#         if self.balance>=wd:
#             self.balance-=wd
#             print(f"New balance after withdraw: {self.balance}")
#             # print(self.balance)
#         else:
#             print("Not a available")


# acc=account('John', 200)
# print(f"\nAccount owner: {acc.owner}, \nBalance: {acc.balance}")
# acc.deposite(50)
# acc.withdraw(75)
# acc.withdraw(300)






#task6 classes
#Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
# import math
# nums=input().split()
# nums=list(map(int, nums))
# prime=list(filter(lambda x: x>1 and all(x%i!=0 for i in range(2, int(math.sqrt(x))+1)) ,nums))
# print(*prime)


