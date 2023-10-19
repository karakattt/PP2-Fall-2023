#functions1 task11
def ispalindrome(word):
    return word==word[::-1]
w=input()

if ispalindrome(w):
    print("Palindrome")
else:
    print("Not a Palindrome")
