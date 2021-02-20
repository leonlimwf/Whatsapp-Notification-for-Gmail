from twilio.rest import Client
from main import main
from collections import deque
import datetime
import time
import config

account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

messages = main()

d1 = deque()
for i in messages:
    d1.append(i)

d2 = deque()
for i in messages:
    d2.append(d1.pop())

myStr = ''
for i in d2:
    myStr += i + '\n\n'

def sendMail():
    send = '\n\n' + myStr
    if (len(myStr) == 0):
        print('No new email found')
    else:
        num = f'whatsapp:{config.num}'
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=send,
            to=num
        )
        print(message.sid)
        
sendMail()

