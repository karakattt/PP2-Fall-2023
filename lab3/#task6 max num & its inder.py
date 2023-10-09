#task6 max num & its inder
a=input().split()
a=[int(n) for n in a]
index=0
for i in range(len(a)):
    if(a[index]<a[i]):
        index=i
        
print(a[index], "",index)
