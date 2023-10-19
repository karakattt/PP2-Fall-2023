#functions1 task4
# prime numbers
def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

def filter(nums):
    prime_nums=[n for n in nums if prime(n)]
    return prime_nums

nums=[1, 2, 3, 4, 5, 7, 11]
prime_nums=filter(nums)
print(*prime_nums)
#print(prime_nums)
