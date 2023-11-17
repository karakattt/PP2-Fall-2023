# task 5 dir file
todolists=['-dinner time', '-to get ready for sleeping', '-checking social media']

file='10.11 evening routine.txt'
# write your text file to input
# file=''

f=open(file, 'w', encoding='utf-8')
for i in todolists:
    f.write(i+"\n")
f.close()

# Checking file
f1=open(file, 'r', encoding='utf-8')
print(f1.read())
f1.close()

