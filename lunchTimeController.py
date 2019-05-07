# This will be the app's main controller.
import os
from pprint import pprint
from EmailService.emailService import EmailService
from DataService.dealAPI import ApiQuery

def test():
    myObj = EmailService()
    apiObj = ApiQuery()
    response = apiObj.getLunch('Lunch')
    #print(isinstance(response, dict))
    message = '\n'
    message += response['businesses'][0]['name']
    message += '\nA ' + response['businesses'][0]['categories'][0]['title'] + ' restaurant' 
    message += '\n Address: ' + response['businesses'][0]['location']['display_address'][0] + response['businesses'][0]['location']['display_address'][1]
    myObj.sendEmail('cs3030pytester@gmail.com', message, 1)
    myObj.end()


test()

