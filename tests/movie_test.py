# Unittest for movie.py

import unittest
from main.movie import *

class TestMovie(unittest.TestCase):

    def setUp(self):
        title = "Test"
        year = 2005
        country = "us"
        actors = ["Woll Smoth", "Dionardo Lecaprio"]
        boxartUrl = "Test"
        ytUrl = "Test"
        self.movie = Movie(title, year, country, actors, boxartUrl, ytUrl)

    def testInstantiation(self):
        self.assertEquals("Test", self.movie.title)
        self.assertEquals(2005, self.movie.year)
        self.assertEquals("us", self.movie.country)
        self.assertEquals(["Woll Smoth", "Dionardo Lecaprio"], self.movie.actors)
        self.assertEquals("Test", self.movie.poster_image_url)
        self.assertEquals("Test", self.movie.trailer_youtube_url)
