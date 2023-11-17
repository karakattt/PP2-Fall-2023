# task 3 dir file
import os
def exists_or_not(path):
    try:
        if os.path.exists(path):
            print("True")

            print(f"File name: {os.path.basename(path)}")
            print(f"Dir name: {os.path.dirname(path)}")
        else: 
            print(path, "doesn't exist")
    except Exception:
        print(f"Error occured: {str(Exception)}")

Path='E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab8'
# write your file and directory to input which have in your PS
# Path=''
exists_or_not(Path)

