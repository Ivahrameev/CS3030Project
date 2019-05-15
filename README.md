# CS3030Project

Dillon Divich and Igor Vahrameev.

This code is for CS3030 Final project

# DataService
This directory contains the code that is capable of querying the yelp api. Install the yelpapi module with *pip install yelpapi*

# EmailService
This directory contains the code for the email client, it both sends email from the dummy test email and checks the email for commands for the service

# User
This directory is where user information is stored. It is capable of updating the file of users.

# Create new user command
To create a new user via email command, do the following. Compose a message to cs3030pytester@gmail.com, with the subject line being exactly 'New user'. The body of the message should be like this:
Username: test
Email: cs3030pytester@gmail.com
Time: 1235
Zip Code: 00000
Preference: lunch

Change the values as desired. 

*To run code, check the command on canvas. The password for the email and the api key must be passed as command line arguments.*