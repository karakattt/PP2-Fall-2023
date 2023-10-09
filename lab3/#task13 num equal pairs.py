#task13 num equal pairs

a=input().split()
a=[str(n) for n in a]
count=0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
            count+=1
print(count)
