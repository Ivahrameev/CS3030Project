# This will be the app's main controller.
import os, threading, time, datetime
from pprint import pprint
from EmailService.emailService import EmailService
from DataService.dealAPI import ApiQuery
from User.user import User
from User.user import getUserIdFromJson

# The services used by controller.
emailService = EmailService()
dataService = ApiQuery()

# This method is the  email checker, who adds the new users to the file. 
def instuctionChecker():
    while(True):
        user = emailService.checkEmailNewUser()
        if user != None:
            print('Adding user!')
            user.writeUserIdToJson()
        time.sleep(60) # Only check once a minute
    print('Checker ending...')

# This method is the main controller. It is what checks the user list and tells the email serivice
# to send the email
def main():
    while(True):
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
    print('Main ending...')

# Threading setup, so we can check and send emails at the same time
mainThread = threading.Thread(target=main)
checkerThread = threading.Thread(target=instuctionChecker)

mainThread.start()
time.sleep(1) # Wait a second between starting threads. 
checkerThread.start()



