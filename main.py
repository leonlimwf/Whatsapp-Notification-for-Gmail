from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
    messages = results.get("messages", [])
    getEmailSubject = []

    pushed = False

    message_count = 10
    for message in messages[:message_count]:
        msg = service.users().messages().get(userId="me", id=message["id"]).execute()
        headers = msg["payload"]["headers"]
        id = msg["id"]

        for i in headers:
            if i["name"] == "Date":
                date = i["value"]
            if i["name"] == "From":
                sender = "✉️ " + i["value"]
            if i["name"] == "Subject":
                subject = "\t➜ " + i["value"]
        mail = date + "\n" + sender + "\n" + subject + "\n"

        checkIfExist = checkId(id)
        if checkIfExist:
            pass
        else:
            writeToFile(id, mail)
            getEmailSubject.append(mail)

    return getEmailSubject


def writeToFile(id, mail):
    f = open("msgId.txt", "a", encoding="utf-8")
    f.write(id + "\n")
    f.close()
    print("Found New Mail: ", mail)


def checkId(id):
    with open("msgId.txt", "r") as file:
        lines = file.read().splitlines()
        if id in lines:
            return True
        else:
            return False
