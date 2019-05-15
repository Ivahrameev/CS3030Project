# This will be the app's main controller.
import os, threading, time, datetime
from pprint import pprint
from EmailService.emailService import EmailService
from DataService.dealAPI import ApiQuery
from User.user import User
from User.user import getUserIdFromJson

emailService = EmailService()
dataService = ApiQuery()

def instuctionChecker():
    i = 1
    while(True):
        print(f'Loop checker {i}')
        user = emailService.checkEmailNewUser()
        if user != None:
            print('Adding user!')
            user.writeUserIdToJson()
        time.sleep(60) # Only check once a minute
        i += 1


def main():
    i = 1
    while(True):
        print(f'Loop main {i}')
        # Update user list each time. 
        userList = getUserIdFromJson()
        # Iterate over the users 
        currentTime = datetime.datetime.now()
        hour, minute = currentTime.hour, currentTime.minute
        for user in userList:
            for key in user.keys():
                tempKey = key
            currentUser = user[tempKey]
            if currentUser['notification time'] == f'{hour}{minute}':
                response = dataService.getData(currentUser['preference'], currentUser['zipcode'], 3)
                message = dataService.makeMessage(response, 3)
                emailService.sendEmail(currentUser['email'], message)
        time.sleep(60)
        i += 1
    print('Main ending...')

mainThread = threading.Thread(target=main)
checkerThread = threading.Thread(target=instuctionChecker)

mainThread.start()
checkerThread.start()


