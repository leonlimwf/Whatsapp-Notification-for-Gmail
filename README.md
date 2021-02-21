# Whatsapp Notification for Gmail

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

```
Gmail OAuth Token: https://developers.google.com/gmail/api/quickstart/python
Python 3 (Reading of email): https://www.python.org/downloads/
Twilio (Sending of Whatsapp Messages): https://www.twilio.com/console
```

### Installing

A step by step series of examples that tell you how to get it running

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib (Python)
pip install twilio
```

### Configuring the files

Head over to config.py file and add in your credentials

```
account_sid = "Twillo API"
auth_token = "Twillo API"
num = "+12345678" # +(Country Code & Your phone number -> No spacing at all)
```

## Running the tests

### In the console

Run the file. It checks for new email every 15 minutes.

```
python run.py
```

### Results (example)

```
No New Email Found

20 Feb 2021 17:25:51 +0800
✉️ test <test@gmail.com>
	➜ is that you Leo>

No New Email Found

20 Feb 2021 17:45:51 +0800
✉️ test <test@gmail.com>
	➜ hey i am gonna...
```

### Built With

- [Twilio](http://www.dropwizard.io/1.0.2/docs/) - For Whatsapp Services
- [Gmail](https://maven.apache.org/) - Gmail API
- [Python](https://rometools.github.io/rome/) - Doing all the awesome stuff :)

## Authors

- **Leo** - [Profile](https://github.com/leonlimwf)
