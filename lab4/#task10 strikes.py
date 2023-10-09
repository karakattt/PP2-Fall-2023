#task10 strikes
n, k = [int(s) for s in input().split()]
workdays=set([d for d in range(1, n+1) if d%7 not in (6,0)])
nostr=set(workdays)

for i in range(k):
    a, b= [int(s) for s in input().split()]
    maxstr=(n-a)//b+1
    nostr-={a+b*k for k in range(maxstr)}
print(len(workdays)-len(nostr))
