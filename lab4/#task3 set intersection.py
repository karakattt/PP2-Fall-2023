#task3 set intersection
a1=input().split()
a1=[int(n) for n in a1]
a2=input().split()
a2=[int(n) for n in a2]

print(*sorted(set(a1)&set(a2)))
