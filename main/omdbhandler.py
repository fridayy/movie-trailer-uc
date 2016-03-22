from urllib.request import *
from urllib.error import URLError
import json

"""
Handles the API calls to the open movie database api (http://www.omdbapi.com/)
and returns the JSON response as a dictonary
"""
class Omdbhandler:
    """
    Queries the open movie database api (http://www.omdbapi.com/)
    and returns the response
    """
    @staticmethod
    def queryopenmoviedatabase(title):
        # replacing whitespace with + for correct api usage
        apititle = title.replace(" ", "+")
        url = "http://www.omdbapi.com/?t={0}&y=&plot=short&r=json".format(apititle)
        try:
            response = urlopen(url).read()
            return response
        except URLError:
            print("Could not reach: {}".format(url))

    """
    Generates a JSON Object from a given HTTP response
    """
    @staticmethod
    def generatejson(response):
        resstring = response.decode('UTF-8')
        data = json.loads(resstring)

        return data

    """
    Returns the movie data gathered from the open movie database as a dictonary
    """
    def getmoviedata(self, withtitle):
        response = self.queryopenmoviedatabase(withtitle)
        data = self.generatejson(response)

        # Raise an Error if the API could not find the movie
        if data['Response'] == "False":
            raise RuntimeError

        return data

