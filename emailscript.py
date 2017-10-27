from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "raspdhr@gmail.com"
toaddr = "dawdiken@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("emailusername", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)