#task8
import re

file=open('row.txt', 'r', encoding='utf-8')
text=file.read()
x=[]
# x=re.findall('[A-Z|А-Я][^A-Z|А-Я]*', text)
x=[s for s in re.split(r"([A-Z|А-Я][^A-Z|А-Я]*)", text) if s]

print(*x)
file.close()
