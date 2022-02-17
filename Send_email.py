#Source = https://www.youtube.com/watch?v=Oz3W-LKfafE&ab_channel=TechWithTim

import smtplib
import ssl
from email.message import EmailMessage

subject = input("Enter Subject:")
body = input("Enter Message:")
sender_email = input("Enter Sender Gmail:")
receiver_email = input("Enter Reciever's Email:")
password = input("Enter Gmail password:")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Sent")
