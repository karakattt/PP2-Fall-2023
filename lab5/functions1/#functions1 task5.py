#functions1 task5
from itertools import permutations
def f(s):
    p=permutations(s)
    for i in list(p):
        print(*i, sep='')
word=input()
f(word)
