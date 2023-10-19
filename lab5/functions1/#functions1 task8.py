#functions1 task8
def contains_007(nums):
    found=[]
    for i in range(0,len(nums)):
        if nums[i]==0:
            for j in range(i+1, len(nums)):
                if nums[j]==0:
                    for k in range(j+1, len(nums)):
                        if nums[k]==7:
                            return True
    
    return False

nums=[int(x) for x in input().split()]
print(contains_007(nums))


