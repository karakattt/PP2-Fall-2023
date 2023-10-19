#functions1 task9
# volume of sphera
def volume(r):
    pi=3.14
    vol=4/3*pi*r*r*r
    return vol
out=volume(int(input()))
print(round(out,2))

