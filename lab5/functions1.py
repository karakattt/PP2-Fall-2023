# functions1 task1
def ounces(gr):
    o=gr*28.3495231
    return o

print(ounces(float(input())))
print(ounces(5))







#functions1 task2
# def toFahrenheit(C):
#     F=C*(9/5)+32
#     return F
# print(toFahrenheit(int(input())))




#functions1 task3
# def solve(head, leg):
#     if head>leg:
#         return "None"
    
#     elif leg%2!=0:
#         return "None"
#     else:
#         r=(leg-2*head)/2
#         ch=head-r
#         return int(r), int(ch)

# print(*solve(35,94))
# # print(solve(35,94))



#functions1 task4
# def prime(n):
#     if n<2:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n%i==0:
#             return False
#     return True

# def filter(nums):
#     prime_nums=[n for n in nums if prime(n)]
#     return prime_nums

# nums=[1, 2, 3, 4, 5, 7, 11]
# prime_nums=filter(nums)
# print(*prime_nums)
# #print(prime_nums)






#functions1 task5
# from itertools import permutations
# def f(s):
#     p=permutations(s)
#     for i in list(p):
#         print(*i, sep='')
# word=input()
# f(word)










#functions1 task6
# def rev(sentence):
#     words=sentence.split()
#     reverse=' '.join(reversed(words))
#     return reverse  
# sent=input()
# print(rev(sent))






#functions1 task7
# def has_33(nums):
#     for i in range(len(nums)-1):
#         if nums[i]==3 and nums[i+1]==3:
#             return True
#     return False

# nums=[int(x) for x in input("Numbers: ").split()] 
# output=has_33(nums)
# print(f"Checking: {output}")






#functions1 task8
# def contains_007(nums):
#     found=[]
#     for i in range(0,len(nums)):
#         if nums[i]==0:
#             for j in range(i+1, len(nums)):
#                 if nums[j]==0:
#                     for k in range(j+1, len(nums)):
#                         if nums[k]==7:
#                             return True
    
#     return False

# nums=[int(x) for x in input().split()]
# print(contains_007(nums))





#functions1 task9
# def volume(r):
#     pi=3.14
#     vol=4/3*pi*r*r*r
#     return vol
# out=volume(int(input()))
# print(round(out,2))






#functions1 task10
# def unique(list_):
#     unique_=[]
#     for i in list_:
#         if i not in unique_:
#             unique_.append(i)
#     return unique_
# a=[int(x) for x in input().split()]
# print(*unique(a))
# # print(unique(a))







#functions1 task11
# def ispalindrome(word):
#     return word==word[::-1]
# w=input()

# if ispalindrome(w):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")






#functions1 task12
# def histogram(list):
#     for i in range(0, len(list)):
#         print('*'*list[i])
# l=[int(x) for x in input().split()]
# histogram(l)
# # histogram([4,9,7])







#functions1 task13
# import random
# def guessingnum():
#     print("Hello! What is your name?")
#     name=input()

#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
#     r=random.randint(1,20)
#     count=0

#     while True:
#         num=int(input("Take a guess. \n"))
#         count+=1
            
#         if num<r:
#             print("\nYour guess is too low.")
#         elif num>r:
#             print("\nYour number is too high.")
#         else:
#             print(f"\nGood job, {name}! You guessed my number in {count} guesses!")
#             break
        
# guessingnum()





#task14 import functions from above 13 tasks
# for example from functions1 task9, use import math
# import math
# def volume(r):
#     pi=3.14
#     vol=4/3*pi*math.pow(r,3)
#     return vol
# out=volume(int(input()))
# print(round(out))
