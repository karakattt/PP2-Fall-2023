#task9
import re 

file=open('row.txt', 'r', encoding='utf-8')
text=file.read()

# if re.search(r'[A-Z]+\s', text):
#     x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2 ", text)
# else:
#     x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2", text)
x=re.sub(r'(\w)([A-Z]|[А-Я])', r"\1 \2", text)
print(x)
file.close()

