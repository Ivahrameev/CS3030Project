# This is where the user object will go

class User():
	def __init__(self, username, email, notificationTime, zipCode, preference):
		self.username = username
		self.email = email
		self.notificationTime = notificationTime
		self.zipCode = zipCode
		self.preference = preference
		
		
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
