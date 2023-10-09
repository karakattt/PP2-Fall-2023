#task16 list queens
N=8
x=[]
y=[]
yes=True
for i in range(N):
    ix, iy=[int(n) for n in input().split()]
    x.append(ix)
    y.append(iy)

for i in range(N):
    for j in range(i+1, N):
        if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])==abs(y[i]-y[j]):
            yes=False

if yes:
    print("NO")
else:
    print("YES")
