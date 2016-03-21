"""
A simple movie data structure which given a certain title will gather
certain additional information from the open movie database API
(http://www.omdbapi.com/)
Thank you omdbapi!

author bnjm
"""

from urllib.request import *
from urllib.error import URLError
import json


class Movie:
    def __init__(self, title, trailer_url):
        self.title = title
        self.year = self.queryopenmoviedatabase(self.title)['Released']
        self.runtime = self.queryopenmoviedatabase(self.title)['Runtime']
        self.genre = self.queryopenmoviedatabase(self.title)['Genre']
        self.country = self.queryopenmoviedatabase(self.title)['Country']
        self.actors = self.queryopenmoviedatabase(self.title)['Actors']
        self.plot = self.queryopenmoviedatabase(self.title)['Plot']
        self.poster_image_url = self.queryopenmoviedatabase(self.title)['Poster']
        self.trailer_youtube_url = trailer_url

    """
    Queries the open movie database api (http://www.omdbapi.com/)
    """
    def queryopenmoviedatabase(self, title):
        # replacing whitespace with + for correct api usage
        apititle = self.title.replace(" ", "+")
        url = "http://www.omdbapi.com/?t={0}&y=&plot=short&r=json".format(apititle)
        # getting the json response from omdbapi
        try:
            response = urlopen(url).read()
        except URLError:
            print("Could not reach: {}".format(url))
        # decode the response to a string
        resstring = response.decode('UTF-8')
        # read json
        data = json.loads(resstring)

        return data
