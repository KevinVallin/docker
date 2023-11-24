import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailhog_host = 'localhost'
mailhog_port = 1025

to_email = 'kevin.vallin@ynov.com'

subject = 'test'
body = 'Ta maman mange des pasteques'
sender_email = 'kevin.vallin@ynov.com'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(mailhog_host, mailhog_port) as server:
    server.sendmail(sender_email, to_email, message.as_string())

print('Voila c\'est envoyer morpion de mes deux')

