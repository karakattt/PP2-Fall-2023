#task12 insert el
a=input().split()
a=[int(n) for n in a]
k,C=[int(s) for s in input().split()]

a.append(0)
for i in range(len(a)-1, k,-1):
    a[i]=a[i-1]

a[k]=C
print(' '.join([str(i) for i in a]))
