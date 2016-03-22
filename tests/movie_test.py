# Unittest for movie.py

import unittest
from unittest.mock import MagicMock

from main.movie import *


class TestMovie(unittest.TestCase):

    def setUp(self):
        title = "Test"
        trailer_url = "http://youtube.com/watch?v=12345"
        self.movie = Movie(title, trailer_url)

    def testMovieCorrectData(self):
        um = MagicMock()
        um.return_value = b'{"Runtime":123}'
        data = um
        print(data)

