#lab6
#generators

#task1 gen
def generate(N):
    for i in range(N):
        yield i**2

N=int(input())
for i in generate(N):
    print(i)
# print(generate(N))




#task2 gen
# def geneven(N):
#     for i in range(N):
#         if i%2==0:
#             yield i

# N=int(input())
# # res = geneven(N)
# n = []
# for ch in geneven(N):
#     n.append(ch)

# print(*n, sep=',')






#task3 gen 
# def divby34(N):
#     for i in range(N):
#         if i%3==0 and i%4==0:
#             yield i

# N=int(input())
# n = []
# for ch in divby34(N):
#     n.append(ch)

# print(*n, sep=', ')





#task4 gen
# def square(n1, n2):
#     for i in range(n1, n2+1):
#         yield i**2

# a=int(input())
# b=int(input())

# for i in square(a,b):
#     print(i, end=' ')






#task5 gen
# def reverse(N):
#     while N>=0:
#         yield N
#         N-=1

# N=int(input())
# for i in reverse(N):
#     print(i, end=' ')