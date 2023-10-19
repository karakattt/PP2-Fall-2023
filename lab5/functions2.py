#functions2
# Dictionary of movies


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






#task2 functions2
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
# def sublist(movies):
#     return [m for m in movies if m["imdb"]>5.5]

# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]

# for m in sublist(movies):
#     print(f" Name: {m['name']};  imdb: {m['imdb']};  Category: {m['category']} ")







#task3 functions2
#Write a function that takes a category name and returns just those movies under that category.
# def returncategory(movies, c):
#     return [m for m in movies if m["category"]==c]

# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]

# cat=input()

# for m in returncategory(movies, cat):
#     print(f" Name: {m['name']};  imdb: {m['imdb']};  Category: {m['category']} ")

# print(returncategory(movies, cat))





#task4 functions2
#Write a function that takes a list of movies and computes the average IMDB score.
# def average(movies):
#     total=0.0

#     for m in movies:
#         total+=m["imdb"]
    
#     if len(movies)>0:
#         avr=total/len(movies)
#         return avr
#     else:
#         return 0.0

# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]

# print(round(average(movies),2))








# #task5 functions2
# #Write a function that takes a category and computes the average IMDB score.
# def average_in_category(movies, c):
#     total=0.0
#     filtered=[m for m in movies if m["category"]==c]

#     for m in filtered:
#         total+=m["imdb"]
    
#     if len(filtered)>0:
#         avr=total/len(filtered)
#         return avr
#     else:
#         return 0.0


# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]

# ct=input()
# print(round(average_in_category(movies, ct), 2))