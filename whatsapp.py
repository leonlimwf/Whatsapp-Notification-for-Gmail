from twilio.rest import Client
from main import main
import datetime
import time
import config


def sendMail():
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)

    messages = main()
    list = []

    for i in messages:
        list.append(i)
    list.reverse()

    myStr = ""
    for i in list:
        myStr += i + "\n\n"

    send = "\n\n" + myStr
    if len(myStr) == 0:
        print("No new email found")
    else:
        num = f"whatsapp:{config.num}"
        message = client.messages.create(
            from_="whatsapp:+14155238886", body=send, to=num
        )


sendMail()
