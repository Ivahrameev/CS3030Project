# This will be the app's main controller.
import os
from EmailService.emailService import EmailService

def test():
	myObj = EmailService()
	myObj.sendEmail('cs3030pytester@gmail.com', 'Hello world')
	myObj.end()

test()