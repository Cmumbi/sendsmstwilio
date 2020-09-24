from dotenv import load_dotenv
load_dotenv()

import os

# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Make API calls here...
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+xxxxxxxxx", 
                       from_="+xxxxxxxxx", 
                       body="You are receiving this message from Twilio.")
