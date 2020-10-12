import os
import json
import smtplib
from email.message import EmailMessage

if os.path.exists(os.getcwd() + "/email.json"):
    with open("./email.json") as f:
        configData = json.load(f)
else:
    configTemplate = {
    "User": "",
    "Password": "",
    "Client": ""
    }

    with open(os.getcwd() + "/email.json", "w+") as f:
        json.dump(configTemplate, f)

client = configData["Client"]


def email_alert(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = configData["User"]
    msg['from'] = user
    password = configData["Password"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert(client, "Testing", "Testing")
