# task 8 dir file
import os
path=r'delete.txt'
if os.path.exists(path):
    # print("exist")
    os.remove(path)
else:
    print("File doesn't exist")