#task3  
import re

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
x=re.findall(r'\w+_\w+', text)
# x=re.findall('[a-z]+_[a-z]+', text)   #2-method(I don't know it's correct or not)
if x:
    a=[]
    for ch in x:
        a.append(ch)
    print(*a, sep="\n")
    print("Found")
else:
    print("Not Found")
file.close()
