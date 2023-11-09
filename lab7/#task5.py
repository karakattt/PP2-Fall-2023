#task5
import re 

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
x=re.findall(r'(.*а.*б\b)', text)
# x=re.findall(r'.*a.*b\b', text)  # for english letters
if x:
    a=[]
    for ch in x:
        a.append(ch)
    print(*a, sep="\n")
    print("Found")
else:
    print("Not Found")
file.close()
