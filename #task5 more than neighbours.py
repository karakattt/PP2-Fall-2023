#task5 more than neighbours
a=input().split()
a=[int(n) for n in a]
count=0
for i in range(1, len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        count+=1

print(count)
