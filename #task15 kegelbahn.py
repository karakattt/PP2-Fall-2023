#task15 kegelbahn
N, k = [int(n) for n in input().split()]

a=['I']*N
for i in range(k):
    l,r = input().split()
    l,r = [int(n) for n in input().split()]
    for j in range(l-1, r):
        a[j]='.'

print(''.join(a))