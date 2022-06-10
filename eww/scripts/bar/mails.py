#!/bin/python

import json
import imaplib
# !todo add more options

# you need a file called "mail.json" in the root of this project
# with format {"mail": "YourMail", "password": "YourPass","server" : "YourServer. eg: imap.gmx.net"}
with open('mail.json') as credentials:
    credentials = json.load(credentials)
    obj = imaplib.IMAP4_SSL(credentials["server"])
    obj.login(credentials["mail"],credentials["password"]) 
    obj.select()
    inbox = len(obj.search(None, 'UnSeen')[1][0].split())
    obj.select("uni")
    uni = len(obj.search(None, 'UnSeen')[1][0].split())
    print(inbox , "", uni)
    obj.close()
    obj.logout()