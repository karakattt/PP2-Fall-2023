#lab7
import re


#task1
file=open('row.txt', 'r', encoding="utf-8")
text = file.read()
p = re.findall('ab*', text) 
# p = re.findall('аб*', text)  # for russian letters
if p:
    print("Found", *p)
else:
    print("Not Found")
file.close()



#?
# with open('row.txt', encoding='utf-8') as file:
#     text=file.read()
#     count=0
#     x=[]
#     for line in file:
#         p=re.findall('ab*', line)
#         if p:
#             x.append(p)
#             count+=1

# print(x, " ", count)
# file.close()



#task2
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()
# p = re.findall('ab{2,3}|аб{2,3}', text) 
# if p:
#     print("Found", *p)
# else:
#     print("Not Found")
# file.close()





#task3  
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()
# x=re.findall(r'\w+_\w+', text)
# # x=re.findall('[a-z]+_[a-z]+', text)   #2-method(I don't know it's correct or not)
# if x:
#     a=[]
#     for ch in x:
#         a.append(ch)
#     print(*a, sep="\n")
#     print("Found")
# else:
#     print("Not Found")
# file.close()





#task4  
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()
# x=re.findall('[A-Z][a-z]+', text)
# # x=re.findall('[А-Я][а-я]+', text) 
# if x:
#     a=[]
#     for ch in x:
#         a.append(ch)
#     print(a)
#     print("Found")
# else:
#     print("Not Found")
# file.close()





#task5
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()
# x=re.findall(r'.*а.*б\b', text)
# # x=re.findall(r'.*a.*b\b', text) 
# if x:
#     a=[]
#     for ch in x:
#         a.append(ch)
#     print(*a, sep="\n")
#     print("Found")
# else:
#     print("Not Found")
# file.close()





#task6
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()
# x=re.sub('[ ,.]', ':', text) 
# print(x)
# file.close()




#task7
# def toCamel(str):
#     cam=re.split('_+', str)
#     res=cam[0]+''.join(map(lambda x: x.title(), cam[1:]))
#     return res

# #if we need to use row.txt, then our calling like this:
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()

# print(toCamel(text))
# file.close()

# #if we don't need to use row.txt, then our calling like this:
# s=str(input())
# print(toCamel(s))

# camel=re.sub('_[a-z][A-Z]', lambda a: a.group(1).upper(), text)





#task8
# file=open('row.txt', 'r', encoding='utf-8')
# text=file.read()
# x=[]
# # x=re.findall('[A-Z|А-Я][^A-Z|А-Я]*', text)
# x=[s for s in re.split(r"([A-Z|А-Я][^A-Z|А-Я]*)", text) if s]

# print(*x)
# file.close()




#task9
# file=open('row.txt', 'r', encoding='utf-8')
# text=file.read()

# # if re.search(r'[A-Z]+\s', text):
# #     x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2 ", text)
# # else:
# #     x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2", text)
# x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2", text)
# print(x)
# file.close()





#task10
# def to_snake(str):
#     sn = re.sub('(.)([A-Z|А-Я][a-z|а-я]+)', r'\1_\2', str)
#     return re.sub('([a-z|а-я0-9])([A-Z|А-Я])', r'\1_\2', sn).lower()

# #if we need to use row.txt, then our calling like this:
# file=open('row.txt', 'r', encoding="utf-8")
# text = file.read()

# print(to_snake(text))
# file.close()

# #if we don't need to use row.txt, then our calling like this:
# s=str(input())
# print(to_snake(s))