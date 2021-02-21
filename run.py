import time
from whatsapp import sendMail


def update():

    while True:
        time.sleep(60 * 15)
        sendMail()


update()
