#task11 knight move конь
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if (x1+1)==x2: 
    if (y1-2)==y2 or (y1+2)==y2:
        print("YES")
    else:
        print("NO")
elif (x1-1)==x2:
    if (y1-2)==y2 or (y1+2)==y2:
        print("YES")
    else:
        print("NO")
elif (x1+2)==x2:
    if (y1-1)==y2 or (y1+1)==y2:
        print("YES")
    else:
        print("NO")
elif (x1-2)==x2:
    if (y1-1)==y2 or (y1+1)==y2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")




# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = abs(x1 - x2)
# dy = abs(y1 - y2)
# if dx == 1 and dy == 2 or dx == 2 and dy == 1:
#     print('YES')
# else:
#     print('NO')
