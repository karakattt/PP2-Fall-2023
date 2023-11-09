#task7
import re

def toCamel(str):
    cam=re.split('_+', str)
    res=cam[0]+''.join(map(lambda x: x.title(), cam[1:]))
    return res

#if we need to use row.txt, then our calling like this:
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()

print(toCamel(text))
file.close()

#if we don't need to use row.txt, then our calling like this:
# s=str(input())
# print(toCamel(s))

# camel=re.sub('_[a-z][A-Z]', lambda a: a.group(1).upper(), text)
