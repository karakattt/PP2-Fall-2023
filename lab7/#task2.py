#task2
import re 

file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
p = re.findall('ab{2,3}|аб{2,3}', text) 
if p:
    print("Found", *p)
else:
    print("Not Found")
file.close()
