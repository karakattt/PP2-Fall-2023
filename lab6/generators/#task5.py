#task5 gen

# desc number from n

def reverse(N):
    while N>=0:
        yield N
        N-=1

N=int(input())
for i in reverse(N):
    print(i, end=' ')