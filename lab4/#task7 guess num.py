#task7 guess num
n=int(input())
nums=set(range(1, n+1))
p=nums

while True:
    find=input()
    if find == "HELP":
        break
    find={int(s) for s in find.split()}
    
    ans=input()
    if ans=="YES":
        p&=find
    else:
        p&=nums-find
print(' '.join([str(x) for x in sorted(p)]))
