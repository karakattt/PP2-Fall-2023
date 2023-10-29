#task1
#generators

#square to N

def generate(N):
    for i in range(N):
        yield i**2

N=int(input())
for i in generate(N):
    print(i, end=' ')
# print(generate(N))
