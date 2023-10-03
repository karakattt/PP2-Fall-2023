#lab1 
#task1 output even index
a=input().split()
a=[int(n) for n in a]

even=[a[i] for i in range(0,len(a), 2)]
print(*even)






#task2 even num
# a=input().split()
# a=[int(n) for n in a]
# for i in range(len(a)):
#     if(a[i]%2==0):
#         print(a[i])






#task3 increasing neighbours
# a=input().split()
# a=[int(n) for n in a]
# for i in range(1, len(a)):
#     if(a[i]>a[i-1]):
#         print(a[i])
#     # elif(







#task4 same sign neighbours
# a=input().split()
# a=[int(n) for n in a]
# for i in range(1, len(a)):
#     if((a[i]<0 and a[i-1]<0) or (a[i]>0 and a[i-1]>0)):
#         print(a[i-1],a[i])
#         break







#task5 more than neighbours
# a=input().split()
# a=[int(n) for n in a]
# count=0
# for i in range(1, len(a)-1):
#     if a[i-1]<a[i]>a[i+1]:
#         count+=1

# print(count)







#task6 max num & its inder
# a=input().split()
# a=[int(n) for n in a]
# index=0
# for i in range(len(a)):
#     if(a[index]<a[i]):
#         index=i
        
# print(a[index], "",index)







#task7 lineup
# a=input().split()
# a=[int(n) for n in a]
# petya=int(input())
# ind=0

# while ind<len(a) and a[ind]>=petya:
#     ind+=1

# print(ind+1)








#task8 num distinct
# a=[int(n) for n in input().split()]
# count=1
# for n in range(0, len(a)-1):
#     if a[n] != a[n+1]:
#         count+=1

# print(count)








#task9 swap neighbours
# a=input().split()
# a=[int(n) for n in a]

# for i in range(0, len(a)-1, 2):
#     a[i], a[i+1]=a[i+1], a[i]

# print(' '.join([str(i) for i in a]))










#task10 swap min max
# a=input().split()
# a=[int(n) for n in a]
# minpos=0
# maxpos=0

# for i in range(1, len(a)):
#     if a[i]>a[maxpos]:
#         maxpos=i
#     if a[i]<a[minpos]:
#         minpos=i

# a[maxpos], a[minpos]=a[minpos], a[maxpos]

# print(' '.join([str(i) for i in a]))







#task11 remove el
# a=input().split()
# a=[int(n) for n in a]

# index=int(input())
# for i in range(index, len(a)-1):
#     a[i]=a[i+1]
        

# a.pop()
# print(' '.join([str(i) for i in a]))








#task12 insert el
# a=input().split()
# a=[int(n) for n in a]
# k,C=[int(s) for s in input().split()]

# a.append(0)
# for i in range(len(a)-1, k,-1):
#     a[i]=a[i-1]

# a[k]=C
# print(' '.join([str(i) for i in a]))









#task13 
# a=input().split()
# a=[str(n) for n in a]
# count=0

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]==a[j]:
#             count+=1
# print(count)







#task14 unique el
# a=input().split()
# a=[int(n) for n in a]

# for i in range(len(a)):
#     for j in range(len(a)):
#         if i!=j and a[i]==a[j]:
#             break
#     else:
#         print(a[i])









#task15 kegelbahn
# N, k = [int(n) for n in input().split()]

# a=['I']*N
# for i in range(k):
#     l,r = input().split()
#     l,r = [int(n) for n in input().split()]
#     for j in range(l-1, r):
#         a[j]='.'

# print(''.join(a))








#task16 list queens
# N=8
# x=[]
# y=[]
# yes=True
# for i in range(N):
#     ix, iy=[int(n) for n in input().split()]
#     x.append(ix)
#     y.append(iy)

# for i in range(N):
#     for j in range(i+1, N):
#         if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])==abs(y[i]-y[j]):
#             yes=False

# if yes:
#     print("NO")
# else:
#     print("YES")
