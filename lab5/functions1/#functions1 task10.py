#functions1 task10
def unique(list_):
    unique_=[]
    for i in list_:
        if i not in unique_:
            unique_.append(i)
    return unique_
a=[int(x) for x in input().split()]
print(*unique(a))
# print(unique(a))
