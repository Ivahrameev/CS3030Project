# This is where the user object will go

import json
import random

data = {}
data['Users'] = ['UserId']

class User():
	
	def __init__(self, username, email, notificationTime, zipCode, preference):
         self.username = username
	 self.email = email
	 self.notificationTime = notificationTime
	 self.zipCode = zipCode
	 self.preference = preference
	 self.uniqueId = random.randint(1,9999999999999)
		
       #this function writes a given user to a json file
       #does not write user with their ID, used to create original 'userList.txt' file
       def writeUserToJson(self):
        data['Users'].append({
         'username' : self.username,
         'email' : self.email,
         'notification time' : self.notificationTime,
         'zipcode' : self.zipCode,
         'preference' : self.preference
        })  
        with open ('userList.txt', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)
           
       #writes the given user to a json file with a unique user id
       #id used for sorting and to prevent old data from being overwritten
       def writeUserIdToJson(self):
        data['Users'].append({self.uniqueId : {
         'username' : self.username, 
         'email' : self.email, 
         'notification time' : self.notificationTime, 
         'zipcode' : self.zipCode, 
         'preference' : self.preference}
        })
        with open ('UserList.txt', 'w') as outfile:
         json.dump(data, outfile, sort_keys=True, indent=4)   
	
       #returns a list with all the users
       #currently only works with 'userList.txt'
       def getUserFromJson(self):
        pulledUser = []
        with open('userList.txt') as json_file:
         data = json.load(json_file)
         for person in data['Users']:
          pulledUser.append({'username':person['username'], 'email':person['email'], 'notification time':person['notification time'], 'zipcode':person['zipcode'], 'preference':person['preference'] })
         return pulledUser
