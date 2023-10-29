#task3 gen 

#div by 3&4

def divby34(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i

N=int(input())
n = []
for ch in divby34(N):
    n.append(ch)

print(*n, sep=', ')
