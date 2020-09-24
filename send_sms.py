# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC8e82b6af85f24aeb2ee9b8b0452b5470", "65adf3363e769ef9c6e2fa43c6a64196")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+254740867393", 
                       from_="+12184526906", 
                       body="Hello World!")