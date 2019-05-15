# Yelp API because groupon hates us...
from yelpapi import YelpAPI # pip3 install yelpapi
import sys

# Service to query yelp. 
class ApiQuery():
    def __init__(self):
        self.yelpApi = YelpAPI(sys.argv[2]) # Create the yelp API, pass the api key too it
        
    # This is how you query the yelp API. 
    def getData(self, term, location, limit):
        response = self.yelpApi.search_query(term=term, location=location, sort_by='rating', limit=limit)
        return response

    # Build the message to send to the user
    def makeMessage(self, response, count):
        message = ''
        for i in range(count):
            message += '\n'
            message += response['businesses'][i]['name']
            message += '\nA ' + response['businesses'][i]['categories'][0]['title'] + ' restaurant' 
            message += '\nAddress: ' + response['businesses'][i]['location']['display_address'][0] + ' ' + response['businesses'][0]['location']['display_address'][1]
            message += '\n'
        return message
