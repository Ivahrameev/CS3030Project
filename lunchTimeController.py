# This will be the app's main controller.
import os, threading, time, datetime
from pprint import pprint
from EmailService.emailService import EmailService
from DataService.dealAPI import ApiQuery
from User.user import User

def test():
    myObj = EmailService()
    apiObj = ApiQuery()
    response = apiObj.getData('Lunch', '80104', 1)
    #print(isinstance(response, dict))
    message = '\n'
    message += response['businesses'][0]['name']
    message += '\nA ' + response['businesses'][0]['categories'][0]['title'] + ' restaurant' 
    message += '\n Address: ' + response['businesses'][0]['location']['display_address'][0] + response['businesses'][0]['location']['display_address'][1]
    #myObj.sendEmail('cs3030pytester@gmail.com', message, 1)
    #myObj.end()
    #user = myObj.checkEmailNewUser()
    #print(user.__dict__)
    print(message)


#test()

emailService = EmailService()
dataService = ApiQuery()

def instuctionChecker():
    while(True):
        user = emailService.checkEmailNewUser()
        if user != None:
            pass # Code to write new user to data

        time.sleep(60) # Only check once a minute

def main():
    userList = [] # add code to read all users
    # FAKE USER FOR TESTING
    userList.append(User('Test', 'cs3030pytester@gmail.com', '23:17', '80104', 'lunch'))
    while(True):
        # Iterate over the users 
        currentTime = datetime.datetime.now()
        hour, minute = currentTime.hour, currentTime.minute
        for user in userList:
            if user.notificationTime == f'{hour}:{minute}':
                response = dataService.getData(user.preference, user.zipCode, 3)
                message = dataService.makeMessage(response, 3)
                emailService.sendEmail(user.email, message)
        time.sleep(60)


mainThread = threading.Thread(target=main)
checkerThread = threading.Thread(target=instuctionChecker)

mainThread.start()
checkerThread.start()


