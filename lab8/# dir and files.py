# lab8
# directories and files

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



# 2-method
# import os

# def list_directories_and_files(path):
#     try:
#         # List all entries (directories and files) in the specified path
#         entries = os.listdir(path)

#         print(f"\nDirectories in {path}:")
#         directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
#         print("\n".join(directories))

#         print(f"\nFiles in {path}:")
#         files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
#         print("\n".join(files))

#         print(f"\nAll Directories and Files in {path}:")
#         print("\n".join(entries))

#     except FileNotFoundError:
#         print(f"The specified path '{path}' does not exist.")
#     except PermissionError:
#         print(f"Permission error accessing '{path}'.")

# # Example usage:
# specified_path = input("Enter the path to list directories and files: ")
# list_directories_and_files(specified_path)







# task 2 dir file
# import os
# path='E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab8'
# # write your file and directory to input which have in your PS
# # path = ''
# print("Exist: ", os.path.exists(path))
# print("Readable: ", os.access(path, os.R_OK))
# print("Writable: ", os.access(path, os.W_OK))
# print("Executable: ", os.access(path, os.X_OK))




# task 3 dir file
# import os
# def exists_or_not(path):
#     try:
#         if os.path.exists(path):
#             print("True")

#             print(f"File name: {os.path.basename(path)}")
#             print(f"Dir name: {os.path.dirname(path)}")
#         else: 
#             print(path, "doesn't exist")
#     except Exception:
#         print(f"Error occured: {str(Exception)}")

# Path='E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab8'
# # write your file and directory to input which have in your PS
# # Path=''
# exists_or_not(Path)




# task 4 dir file
# file='10.11.txt'
# # write your text file to input
# # file=''
# with open(file, 'r', encoding='utf-8') as f:
#     print(f"Number of lines in {f.name} is {len(f.readlines())}")
# f.close()






# task 5 dir file
# todolists=['-dinner time', '-to get ready for sleeping', '-checking social media']

# file='10.11 evening routine.txt'
# # write your text file to input
# # file=''

# f=open(file, 'w', encoding='utf-8')
# for i in todolists:
#     f.write(i+"\n")
# f.close()

# # Checking file
# f1=open(file, 'r', encoding='utf-8')
# print(f1.read())
# f1.close()




# task 6 dir file
# import os, string
# if not os.path.exists("Alphabet"):
#     os.makedirs("Alphabet")
# for letter in string.ascii_uppercase:
#     file_path=os.path.join("Alphabet", f"{letter}.txt")
#     with open(file_path, 'w') as f:
#         f.writelines(letter)
# print("Generating 26 text files is done")






# task 7 dir file
# You can also put in input your text file as first and second file
# with open('1.txt', 'r', encoding='utf-8') as f1, open('2.txt', 'a', encoding='utf-8') as f2:
#     for i in f1:
#         f2.write(i)

# # Checking
# f1=open('1.txt', 'r', encoding='utf-8')
# print('First file: ',f1.read())
# f1.close()

# f2=open('2.txt', 'r', encoding='utf-8')
# print('Second file: ',f2.read())
# f2.close()






# task 8 dir file
# import os
# path=r'delete.txt'
# if os.path.exists(path):
#     # print("exist")
#     os.remove(path)
# else:
#     print("File doesn't exist")