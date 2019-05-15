# Yelp API because groupon hates us...

from yelpapi import YelpAPI
import sys

class ApiQuery():
    def __init__(self):
        self.yelpApi = YelpAPI(sys.argv[2])
        
    def getData(self, term, location, limit):
        response = self.yelpApi.search_query(term=term, location=location, sort_by='rating', limit=limit)
        return response

    def makeMessage(self, response, count):
        message = ''
        for i in range(count):
            message += '\n'
            message += response['businesses'][i]['name']
            message += '\nA ' + response['businesses'][i]['categories'][0]['title'] + ' restaurant' 
            message += '\n Address: ' + response['businesses'][i]['location']['display_address'][0] + response['businesses'][0]['location']['display_address'][1]
            message += '\n'
        return message
