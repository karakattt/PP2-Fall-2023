#task8 num distinct
a=[int(n) for n in input().split()]
count=1
for n in range(0, len(a)-1):
    if a[n] != a[n+1]:
        count+=1

print(count)
