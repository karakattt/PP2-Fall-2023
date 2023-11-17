# task2 built in function
# # from curses.ascii import islower
def calculating_upper_lower(s):
    count_upper=0
    count_lower=0
    for ch in s:
        if ch.isupper() :
            count_upper+=1
        elif ch.islower():
            count_lower+=1
        else:
            pass
    return f'Capitals: {count_upper} \nLowers: {count_lower}'

word=str(input())
print(calculating_upper_lower(word))
