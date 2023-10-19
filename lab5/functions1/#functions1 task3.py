#functions1 task3
# calculate how many chickens and rabbits
def solve(head, leg):
    if head>leg:
        return "None"
    
    elif leg%2!=0:
        return "None"
    else:
        r=(leg-2*head)/2
        ch=head-r
        return int(r), int(ch)

print(*solve(35,94))
# print(solve(35,94))
