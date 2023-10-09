#task3 increasing neighbours
a=input().split()
a=[int(n) for n in a]
for i in range(1, len(a)):
    if(a[i]>a[i-1]):
        print(a[i])
