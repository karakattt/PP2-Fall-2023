# task 4 dir file
file='10.11.txt'
# write your text file to input
# file=''
with open(file, 'r', encoding='utf-8') as f:
    print(f"Number of lines in {f.name} is {len(f.readlines())}")
f.close()

