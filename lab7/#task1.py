#task1
import re

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
p = re.findall('ab*', text) 
# p = re.findall('аб*', text)  # for russian letters
if p:
    print("Found", *p)
else:
    print("Not Found")
file.close()
