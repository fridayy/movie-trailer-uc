#!/usr/bin/pyhton3
# main.py
# author: bnjm

from main.fresh_tomatoes import *
from main.movie import *




aBittersweetLife = Movie("A Bittersweet Life",
                         "https://www.youtube.com/watch?v=0P4YG73KHHo")

oldboy = Movie("Oldboy",
               "https://www.youtube.com/watch?v=2HkjrJ6IK5E")

isawthedevil = Movie("I Saw The Devil",
                     "https://www.youtube.com/watch?v=xwWgp1bqVwE")

movies = []
movies.append(aBittersweetLife)
movies.append(oldboy)
movies.append(isawthedevil)
open_movies_page(movies)
