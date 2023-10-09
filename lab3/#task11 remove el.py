#task11 remove el
a=input().split()
a=[int(n) for n in a]

index=int(input())
for i in range(index, len(a)-1):
    a[i]=a[i+1]
        

a.pop()
print(' '.join([str(i) for i in a]))
