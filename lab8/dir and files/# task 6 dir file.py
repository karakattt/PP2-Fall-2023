# task 6 dir file
import os, string
if not os.path.exists("Alphabet"):
    os.makedirs("Alphabet")
for letter in string.ascii_uppercase:
    file_path=os.path.join("Alphabet", f"{letter}.txt")
    with open(file_path, 'w') as f:
        f.writelines(letter)
print("Generating 26 text files is done")
