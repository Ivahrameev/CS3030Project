# This is where the user object will go

class User():
	def __init__(self, username, email, notificationTime, zipCode, preference):
		self.username = username
		self.email = email
		self.notificationTime = notificationTime
		self.zipCode = zipCode
		self.preference = preference
		
       #this function writes a given user to a json file
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
	
       #returns a list with all the users
       def getUserFromJson(self):
        pulledUser = []
        with open('userList.txt') as json_file:
         data = json.load(json_file)
         for person in data['Users']:
          pulledUser.append({'username':person['username'], 'email':person['email'], 'notification time':person['notification time'], 'zipcode':person['zipcode'], 'preference':person['preference'] })
         return pulledUser
