# This is where the user object will go
import json, os, random

# File path, since this code is run outside of this directory, it needs to be updated. 
filePath = os.path.join(os.getcwd(), 'User', 'UserList.txt')

# User data
data = {}
data['Users'] = []
# User class, creates users and adds users to list stored in text file
class User():
    def __init__(self, username, email, notificationTime, zipCode, preference):
        self.username = username
        self.email = email
        self.notificationTime = notificationTime
        self.zipCode = zipCode
        self.preference = preference
        self.uniqueId = self.generateUniqueId()
        
        
    def generateUniqueIdDecorator(func):
        def wrapper(self):
            print("Generating a unique User Id for [" + self.username + "]...")
            return func(self)
        return wrapper
       
    @generateUniqueIdDecorator
    def generateUniqueId(self):
        random.seed()
        numberList = [] 
        listChoice = []
        number = []
        divisorList = [1,10,100,1000,10000]
        #generates 1000 random numbers
        for x in range(1000): 
            numberList.append(random.randint(1,9999999999)) 
        #randomly picks 100 of the 1000 numbers
        for x in range(100): 
            listChoice.append(random.choice(numberList))
        #generates an number from four other numbers via a lambda function
        randomNumber = lambda NumA, NumB, DivisorA, DivisorB : NumA/DivisorA + NumB/DivisorB 
        #generates ten random numbers by picking two numbers from a list of 
        #randomly generated numbers and randomly picks two divisors from a list
        for x in range(10):
            number.append(randomNumber(random.choice(listChoice),
                                 random.choice(listChoice),
                                 random.choice(divisorList),
                                 random.choice(divisorList)))
        #returns a very random integer that is generated from four other numbers
        return int(randomNumber(random.choice(number), 
                             random.choice(number), 
                             random.choice(divisorList),
                             random.choice(divisorList)))
      
    
    def writeUserIdToJsonDecorator(func):
        def wrapper(self):
            print("Writing user [" + self.username + "] to file with ID: " + str(self.uniqueId) +"...")
            func(self)
            print("...User [" + self.username + "] successfully written to file\n")
        return wrapper 
    
    
    #writes the given user to a json file with a unique user id
    #id used for sorting and to prevent old data from being overwritten
    @writeUserIdToJsonDecorator
    def writeUserIdToJson(self):
        global data
        data['Users'].append({self.uniqueId : {
        'username' : self.username, 
        'email' : self.email, 
        'notification time' : self.notificationTime, 
        'zipcode' : self.zipCode, 
        'preference' : self.preference}
        })
        with open (filePath, 'w') as outfile:
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

    
    
#returns a dictionary of the user base
#will work with both the old and new 'UserList.txt' file
def getUserIdFromJson():
    global data
    with open(filePath) as json_file:
        data = json.load(json_file)
    return data['Users']
