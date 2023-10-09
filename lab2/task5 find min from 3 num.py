#task5 find min from 3 num
arr=[]
min=1e9

for i in range(3):
    a=int(input())
    arr.append(a)

for a in arr:
    if a<min:
        min=a
print(min)

# a = int(input())
# b = int(input())
# c = int(input())
# if b >= a <= c:
#     print(a)
# elif a >= b <= c:
#     print(b)
# else:
#     print(c)
