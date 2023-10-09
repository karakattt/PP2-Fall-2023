# #task2 num of coincidental
a1=input().split()
a1=[int(n) for n in a1]
a2=input().split()
a2=[int(n) for n in a2]
b=set(a1+ a2)

print((len(a1)+len(a2))-len(b))

# print(len(set(a1)&set(a2)))
