import smtplib, pyzmail, re
from imapclient import IMAPClient
imaplib._MAXLINE = 10000000 # Size limit for search



# Email Service class will take emails, send them, check emails for instructions.
class EmailService():
	def __init__(self):
		# Set up the Imap client, and log in.
		self.imapObj= IMAPClient('imap.gmail.com', ssl=True) 
		print(self.imapObj.login('cs3030pytester@gmail.com', sys.argv[1])) # Change to read from encrypted file
		self.imapObj.select_folder('INBOX')

	# Send Email will validate email, compose message, send. Return True if sent, False if not
	def sendEmail(self, email, message):
		# Check if email is valid
		emailRegex = re.compile('\S+@\S+')
		if emailRegex.findall(email) == None:
			print("Error: Invalid Email.")
			return False

		# Set up email 
