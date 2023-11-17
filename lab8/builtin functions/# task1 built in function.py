# task1 built in function
def multipleList(nums):
    res=1
    for i in nums:
        res*=i
    return res

a=input()
nums_list=[int(i) for i in a.split()]
print(multipleList(nums_list))
