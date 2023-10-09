#task4 same sign neighbours
a=input().split()
a=[int(n) for n in a]
for i in range(1, len(a)):
    if((a[i]<0 and a[i-1]<0) or (a[i]>0 and a[i-1]>0)):
        print(a[i-1],a[i])
        break
