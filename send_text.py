from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfa453efad70b9e86ad8f9fe7cdc6feab"  # Create account on twilio websit and copy and paste your acc_sid and aut_token
auth_token = "f2cab17213ec8362179caf091600a8f5"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Pandey if you get this message then please inform Rohan )",
to="+16602382434", # Replace with your phone number
from_="+16602624892") # Replace with your Twilio number

print message.sid
