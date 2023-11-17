#lab8 

# task1 built in function
def multipleList(nums):
    res=1
    for i in nums:
        res*=i
    return res

a=input()
nums_list=[int(i) for i in a.split()]
print(multipleList(nums_list))




# task2 built in function
# # # from curses.ascii import islower
# def calculating_upper_lower(s):
#     count_upper=0
#     count_lower=0
#     for ch in s:
#         if ch.isupper() :
#             count_upper+=1
#         elif ch.islower():
#             count_lower+=1
#         else:
#             pass
#     return f'Capitals: {count_upper} \nLowers: {count_lower}'

# word=str(input())
# print(calculating_upper_lower(word))




# task3 built in function
# def isPalindrome(s):
#     return s==s[::-1]

# word=input()
# print(isPalindrome(word))




# task4 built in function
# import math 
# import time

# def squareroot(num, ms):
#     time.sleep(ms/1000.0)
#     return float(math.sqrt(num))

# number=int(input())
# milisec=int(input())
# res=squareroot(number, milisec)
# print(f"Square root of {number} after {milisec} miliseconds is {res}")





# task5 built in function
# def isTrue(tuple):
#     return all(tuple)

# # Inputs
# t=(True, False, True)
# print(f"All elements of the tuple are true: {isTrue(t)}")
