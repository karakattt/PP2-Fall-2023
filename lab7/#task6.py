#task6
import re

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
x=re.sub('[ ,.]', ':', text) 
print(x)
file.close()
