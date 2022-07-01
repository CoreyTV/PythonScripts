import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#you have to turn off Less secure apps on your google acocunt
#I actually have one of these clients in java for my home server for notifying me when something is down
to = "replace this with who you want to send it to"
#login below
email = "replace this with email address"
password = "replace this with password here"
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to
msg['Subject'] = "My SMTP client"
msg.attach(MIMEText("it works!", 'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
server.sendmail(email, to, text)
server.quit()
print("sent")
