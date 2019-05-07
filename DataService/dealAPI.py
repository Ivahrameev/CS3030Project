# Yelp API because groupon hates us...

from yelpapi import YelpAPI
import sys

class ApiQuery():
    def __init__(self):
        self.yelpApi = YelpAPI(sys.argv[2])
        

    def getLunch(self, term):
        
        response = self.yelpApi.search_query(term=term, location='colorado spring, co', sort_by='rating', limit=1)
        return response
