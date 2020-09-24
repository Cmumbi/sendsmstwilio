#This project demonstrates how to send an SMS to a phone number using Twilio's API, code written in Python.

#How to install...
i) Clone/download the project to your local machine.
ii) Run your terminal and cd into the root directory.
iii) Create and activate a virtualenv.
iv) Run command "pip install -r requirements.txt" to install project requirements.

#How to access Twilio's API...
i) On your browser, go to https://www.twilio.com/.
ii) Sign up for a trial account or log in if you already have one.
iii) On the user dashboard, take note of your Account SID, Auth Token and Twilio Phone Number.

#How to run the project...
i) In the root directory, create a .env file where you will store your Account SID under 'TWILIO_ACCOUNT_SID' and Auth Token under 'TWILIO_AUTH_TOKEN' variables. Remember to add this file to .gitignore if to be used in production.
ii) Comments in the code should direct you further on how to utilize the API.
iii) Once you have set all your credentials, in your terminal, run command "python send_sms.py".
iv) A message should be sent to the recipient number.