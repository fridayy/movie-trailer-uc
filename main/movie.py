"""
A simple movie data structure
author bnjm
"""
from main.omdbhandler import *


class Movie:
    def __init__(self, title, trailer_url):
        self.title = title
        omdb = Omdbhandler()
        __data = omdb.getmoviedata(title)
        self.year = __data['Released']
        self.runtime = __data['Runtime']
        self.genre = __data['Genre']
        self.country = __data['Country']
        self.actors = __data['Actors']
        self.plot = __data['Plot']
        self.poster_image_url = __data['Poster']
        self.trailer_youtube_url = trailer_url

