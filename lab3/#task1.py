#task1 output even index
a=input().split()
a=[int(n) for n in a]

even=[a[i] for i in range(0,len(a), 2)]
print(*even)
