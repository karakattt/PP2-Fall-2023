#lab2 

#task1 find min num
x=int(input())
y=int(input())
if x>y:
    print(y)
else:
    print(x)





#task2 sign(x)
# a=int(input())
# if a>0:
#     print(1)
# elif a<0:
#     print(-1)
# else:
#     print(0)







#task3 chessboard
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())

# if (x1+y1)%2==(x2+y2)%2:
#     print("YES")
# else:
#     print("NO")







#task4 leap year
# year=int(input())
# if year%4==0 and year%100!=0:
#     print("YES")
# elif year%400==0:
#     print("YES")
# else:
#     print("NO")







#task5 find min from 3 num
# arr=[]
# min=1e9

# for i in range(3):
#     a=int(input())
#     arr.append(a)

# for a in arr:
#     if a<min:
#         min=a
# print(min)








#task6 do they match?
# a=int(input())
# b=int(input())
# c=int(input())

# if a==b==c:
#     print(3)
# elif a==b or b==c or a==c:
#     print(2)
# elif a!=b and a!=c and b!=c:
#     print(0)












#task7 rook_move
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())

# if x1==x2 or y1==y2:
#     print("YES")
# else:
#     print("NO")







#task8 king move
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())
# dx=abs(x1-x2)
# dy=abs(y1-y2)

# if dx==dy==1 or (x1==x2 and dy==1) or (y1==y2 and dx==1):
#     print("YES")
# else:
#     print("NO")










#task9 bishop move слон
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())
# dx=abs(x1-x2)
# dy=abs(y1-y2)

# if dy==dx:
#     print("YES")
# else:
#     print("NO")








#task10 queen move ферзь
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())
# dx=abs(x1-x2)
# dy=abs(y1-y2)


# if x1==x2 or y1==y2 or dx==dy:
#     print("YES")
# else:
#     print("NO")











#task11 knight move конь
# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())

# if (x1+1)==x2: 
#     if (y1-2)==y2 or (y1+2)==y2:
#         print("YES")
#     else:
#         print("NO")
# elif (x1-1)==x2:
#     if (y1-2)==y2 or (y1+2)==y2:
#         print("YES")
#     else:
#         print("NO")
# elif (x1+2)==x2:
#     if (y1-1)==y2 or (y1+1)==y2:
#         print("YES")
#     else:
#         print("NO")
# elif (x1-2)==x2:
#     if (y1-1)==y2 or (y1+1)==y2:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")








#task12 piece of chocolate 
# n=int(input())
# m=int(input())
# k=int(input())

# if (k%n==0 and k//n<=m) or (k%m==0 and k//m<=n):
#     print("YES")
# else:
#     print("NO")









#task13 how many metres?
# n=int(input())
# m=int(input())
# x=int(input())
# y=int(input())

# if n>m:
#     n, m=m, n
# if x>=n/2:
#     x=n-x
# if y>=m/2:
#     y=m-y

# if x<y:
#     print(x)
# else:
#     print(y)