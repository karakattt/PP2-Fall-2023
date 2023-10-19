#functions1 task6
def rev(sentence):
    words=sentence.split()
    reverse=' '.join(reversed(words))
    return reverse  
sent=input()
print(rev(sent))
