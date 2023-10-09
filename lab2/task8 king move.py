#task8 king move
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
dx=abs(x1-x2)
dy=abs(y1-y2)

if dx==dy==1 or (x1==x2 and dy==1) or (y1==y2 and dx==1):
    print("YES")
else:
    print("NO")
