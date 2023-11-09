#task10
import re

def to_snake(str):
    sn = re.sub('(.)([A-Z|А-Я][a-z|а-я]+)', r'\1_\2', str)
    return re.sub('([a-z|а-я0-9])([A-Z|А-Я])', r'\1_\2', sn).lower()

#if we need to use row.txt, then our calling like this:
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()

print(to_snake(text))
file.close()

#if we don't need to use row.txt, then our calling like this:
# s=str(input())
# print(to_snake(s))