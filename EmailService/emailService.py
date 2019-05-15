import smtplib, pyzmail, re, sys, datetime, imaplib, pyzmail
from imapclient import IMAPClient
imaplib._MAXLINE = 10000000 # Size limit for search

from User.user import User

# Email Service class will take emails, send them, check emails for instructions.
class EmailService():
    def __init__(self):
        # Set up the Imap client, and log in. Will be used for email searching
        self.email = 'cs3030pytester@gmail.com'
        self.imapObj= IMAPClient('imap.gmail.com', ssl=True) 
        print(self.imapObj.login(self.email, sys.argv[1])) # Change to read from encrypted file
        self.imapObj.select_folder('INBOX')

        # Set up SMTP stuff, this is what will send the email.
        self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        print(self.smtpObj.starttls())
        print(self.smtpObj.login(self.email, sys.argv[1]))


    # Send Email will validate email, compose message, send. Return True if sent, False if not
    def sendEmail(self, email, message):
        # Check if email is valid
        emailRegex = re.compile('\S+@\S+')
        if emailRegex.findall(email) == None:
            print("Error: Invalid Email.")
            return False

        # Set up email 
        date = datetime.datetime.now().strftime('%m-%d-%y')
        composedMessage = f'Subject: Your lunch ideas {date} \n\n Checkout these places: {message}'
        self.smtpObj.sendmail(self.email, email, composedMessage)
        print("Email sent to " + email)

    # Check email if there is a request for a new user
    def checkEmailNewUser(self):
        self.imapObj.noop()
        UIDs = self.imapObj.search(['SUBJECT', 'New user', 'UNSEEN']) # Find the emails
        if len(UIDs) == 0:
            return None
        lastUID = UIDs[len(UIDs)-1]
        rawMessages= self.imapObj.fetch(lastUID, ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessages[lastUID][b'BODY[]'])
        body = message.text_part.get_payload().decode("utf-8")
        userinfo = body.splitlines()
        return User(userinfo[0].strip("Username: "), message.get_addresses('from')[0][1], userinfo[2].strip("Time: "), userinfo[3].strip("Zip Code: "), userinfo[4].strip("Preference: "))

    def end(self):
        self.smtpObj.quit()
        self.imapObj.logout()

