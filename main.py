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

wargames = Movie("WarGames",
                 "https://www.youtube.com/watch?v=tAcEzhQ7oqA")

movies = [aBittersweetLife, oldboy, isawthedevil, wargames]
open_movies_page(movies)
