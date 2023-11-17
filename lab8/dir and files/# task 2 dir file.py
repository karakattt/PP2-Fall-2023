# task 2 dir file
import os
path='E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab8'
# write your file and directory to input which have in your PS
# path = ''
print("Exist: ", os.path.exists(path))
print("Readable: ", os.access(path, os.R_OK))
print("Writable: ", os.access(path, os.W_OK))
print("Executable: ", os.access(path, os.X_OK))

