# task 1 dir file
import os
path='E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab8'
# write your file and directory to input which have in your PS
# path = ''

print("Directories: ")
print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
print("Files: ")
print([x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))])
print("Both files and directories: ")
print([x for x in os.listdir(path)])


# My Output was
# Directories: 
# ['Alphabet', 'builtin functions', 'dir and files']
# Files:
# ['# builtin functions.py', '# dir and files.py', '1.txt', '10.11 evening routine.txt', '10.11.txt', '2.txt', 'delete.txt']
# Both files and directories:
# ['# builtin functions.py', '# dir and files.py', '1.txt', '10.11 evening routine.txt', '10.11.txt', '2.txt', 'Alphabet', 'builtin functions', 'delete.txt', 'dir and files']