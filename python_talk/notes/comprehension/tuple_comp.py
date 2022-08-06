movies = [("Citizen Kane", 1941, 4.0), ("The Aviator", 2004, 4.9), ("No Country For Old Man", 2007, 4.5),
          ("The Lord of the Rings: The Fellowship of the Ring", 2001, 5.0), ("Groundhog Day", 1993, 4.4)]

pre2k = [name for (name,year,rating) in movies if year < 2000]
# ['Citizen Kane', 'Groundhog Day']


best_movies = [{name:rating} for (name,year,rating) in movies if rating > 4.5]
# [{'The Aviator': 4.9}, {'The Lord of the Rings: The Fellowship of the Ring': 5.0}]

