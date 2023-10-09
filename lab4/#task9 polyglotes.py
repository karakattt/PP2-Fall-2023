#task9 polyglotes
stu=[{input() for j in range(int(input()))} for i in range(int(input()))]

everyknow=set.intersection(*stu)
anyknow=set.union(*stu)

print(len(everyknow))
for i in sorted(everyknow):
    print(i)

print(len(anyknow))
for k in sorted(anyknow):
    print(k)

