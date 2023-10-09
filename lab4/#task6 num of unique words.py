#task6 num of unique words
n=int(input())
u_w=set()
for i in range(n):
    u_w.update(input().split())

print(len(u_w))
