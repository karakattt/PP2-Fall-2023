#task8 guess num 2
n=int(input())
nums=set(range(1, n+1))
p=nums

while True:
    find=input()
    if find == "HELP":
        break
    find={int(s) for s in find.split()}
    
    if len(p&find)>len(p)/2:
        print("YES")
        p&=find
    else:
        print("NO")
        p&=nums-find
print(' '.join([str(x) for x in sorted(p)]))
