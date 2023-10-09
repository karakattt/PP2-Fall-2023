#lab4 


#task1 num of unique
a=input().split()
a=[int(n) for n in a]
b=set(a)
print(len(b))





# #task2 num of coincidental
# a1=input().split()
# a1=[int(n) for n in a1]
# a2=input().split()
# a2=[int(n) for n in a2]
# b=set(a1+ a2)

# print((len(a1)+len(a2))-len(b))

# # print(len(set(a1)&set(a2)))






#task3 set intersection
# a1=input().split()
# a1=[int(n) for n in a1]
# a2=input().split()
# a2=[int(n) for n in a2]

# print(*sorted(set(a1)&set(a2)))






#task4 occurs before
# a=input().split()
# unique={}

# for i in a:
#     if i in unique:
#         print("YES")
#     else:
#         print("NO")
#         unique[i]=True;







#task5 cubes
# n, m =[int(s) for s in input().split()]
# a=set()
# b=set()

# for i in range(n):
#     a.add(int(input()))
# for i in range(m):
#     b.add(int(input()))

# print(len(a&b))
# print(*sorted(a&b))
# print(len(a-b))
# print(*sorted(a-b))
# print(len(b-a))
# print(*sorted(b-a))







#task6 num of unique words
# n=int(input())
# u_w=set()
# for i in range(n):
#     u_w.update(input().split())

# print(len(u_w))







#task7 guess num
# n=int(input())
# nums=set(range(1, n+1))
# p=nums

# while True:
#     find=input()
#     if find == "HELP":
#         break
#     find={int(s) for s in find.split()}
    
#     ans=input()
#     if ans=="YES":
#         p&=find
#     else:
#         p&=nums-find
# print(' '.join([str(x) for x in sorted(p)]))








#task8 guess num 2
# n=int(input())
# nums=set(range(1, n+1))
# p=nums

# while True:
#     find=input()
#     if find == "HELP":
#         break
#     find={int(s) for s in find.split()}
    
#     if len(p&find)>len(p)/2:
#         print("YES")
#         p&=find
#     else:
#         print("NO")
#         p&=nums-find
# print(' '.join([str(x) for x in sorted(p)]))






#task9 polyglotes
# stu=[{input() for j in range(int(input()))} for i in range(int(input()))]

# everyknow=set.intersection(*stu)
# anyknow=set.union(*stu)

# print(len(everyknow))
# for i in sorted(everyknow):
#     print(i)

# print(len(anyknow))
# for k in sorted(anyknow):
#     print(k)










#task10 strikes
# n, k = [int(s) for s in input().split()]
# workdays=set([d for d in range(1, n+1) if d%7 not in (6,0)])
# nostr=set(workdays)

# for i in range(k):
#     a, b= [int(s) for s in input().split()]
#     maxstr=(n-a)//b+1
#     nostr-={a+b*k for k in range(maxstr)}
# print(len(workdays)-len(nostr))
