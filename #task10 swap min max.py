#task10 swap min max
a=input().split()
a=[int(n) for n in a]
minpos=0
maxpos=0

for i in range(1, len(a)):
    if a[i]>a[maxpos]:
        maxpos=i
    if a[i]<a[minpos]:
        minpos=i

a[maxpos], a[minpos]=a[minpos], a[maxpos]

print(' '.join([str(i) for i in a]))
