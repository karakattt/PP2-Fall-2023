# task4 how much time
n=int(input())
hour=n//60
minute=n%60

if hour>23: 
    hour=hour%24

print(hour, minute)
