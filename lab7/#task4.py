#task4  
import re

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
x=re.findall('[A-Z][a-z]+', text)
# x=re.findall('[А-Я][а-я]+', text) 
if x:
    a=[]
    for ch in x:
        a.append(ch)
    print(a)
    print("Found")
else:
    print("Not Found")
file.close()
