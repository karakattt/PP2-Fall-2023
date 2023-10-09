#task14 unique el
a=input().split()
a=[int(n) for n in a]

for i in range(len(a)):
    for j in range(len(a)):
        if i!=j and a[i]==a[j]:
            break
    else:
        print(a[i])
