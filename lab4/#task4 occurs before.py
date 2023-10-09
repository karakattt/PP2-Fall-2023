#task4 occurs before
a=input().split()
unique={}

for i in a:
    if i in unique:
        print("YES")
    else:
        print("NO")
        unique[i]=True;
