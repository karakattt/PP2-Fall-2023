#functions1 task13
import random
def guessingnum():
    print("Hello! What is your name?")
    name=input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    r=random.randint(1,20)
    count=0

    while True:
        num=int(input("Take a guess. \n"))
        count+=1
            
        if num<r:
            print("\nYour guess is too low.")
        elif num>r:
            print("\nYour number is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {count} guesses!")
            break
        
guessingnum()
