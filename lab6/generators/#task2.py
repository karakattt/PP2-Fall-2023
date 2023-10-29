#task2 gen

# prime from 0 to n

def geneven(N):
    for i in range(N):
        if i%2==0:
            yield i

N=int(input())
# res = geneven(N)
n = []
for ch in geneven(N):
    n.append(ch)

print(*n, sep=',')
