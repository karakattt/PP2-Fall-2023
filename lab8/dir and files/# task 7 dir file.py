# task 7 dir file
# You can also put in input your text file as first and second file
with open('1.txt', 'r', encoding='utf-8') as f1, open('2.txt', 'a', encoding='utf-8') as f2:
    for i in f1:
        f2.write(i)

# Checking
f1=open('1.txt', 'r', encoding='utf-8')
print('First file: ',f1.read())
f1.close()

f2=open('2.txt', 'r', encoding='utf-8')
print('Second file: ',f2.read())
f2.close()


