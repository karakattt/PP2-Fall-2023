#task1 functions2
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def isabove_55(movie):
    if movie["imdb"]>5.5:
        return True
    else: return False

movie = {
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}

print(isabove_55(movie))
