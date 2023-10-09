#task7 lineup
a=input().split()
a=[int(n) for n in a]
petya=int(input())
ind=0

while ind<len(a) and a[ind]>=petya:
    ind+=1

print(ind+1)
