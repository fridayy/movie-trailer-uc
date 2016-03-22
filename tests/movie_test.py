# Unittest for movie.py

import unittest

from main.movie import *


class TestMovie(unittest.TestCase):

    def testInvalidTitle(self):
        print("Testing invalid Title")
        with self.assertRaises(RuntimeError):
            m = Movie("d1hd1872d7g2", "213d12d")




