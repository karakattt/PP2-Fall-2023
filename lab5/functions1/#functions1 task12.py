#functions1 task12
def histogram(list):
    for i in range(0, len(list)):
        print('*'*list[i])
l=[int(x) for x in input().split()]
histogram(l)
# histogram([4,9,7])
