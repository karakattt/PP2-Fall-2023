#task2 even num
a=input().split()
a=[int(n) for n in a]
for i in range(len(a)):
    if(a[i]%2==0):
        print(a[i])
