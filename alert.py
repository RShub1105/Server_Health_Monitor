import requests, smtplib
from email.mime.text import MIMEText

SLACK_WEBHOOK = ""  # add webhook
SENDER = "your_email@gmail.com"
PASSWORD = "your_app_password"
RECEIVER = "receiver@gmail.com"

def send_slack(message):
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={"text": message})

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"], msg["From"], msg["To"] = subject, SENDER, RECEIVER
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(); server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECEIVER, msg.as_string())