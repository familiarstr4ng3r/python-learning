# https://www.youtube.com/watch?v=mWZYn5I_jkY
# or simple version:
# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

# https://www.youtube.com/watch?v=YPiHBtddefI

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

email = 'dmitriyclashofclans@gmail.com'
password = ''

to_mail = 'mosifim625@tdcryo.com'

# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # or SMTP()
server.ehlo() # or starttls()
server.login(email, password)

message = MIMEMultipart()
message['From'] = 'Familiar Stranger'
message['To'] = to_mail
message['Subject'] = 'Hello world'

message_content = 'Message with Python'

message.attach(MIMEText(message_content, 'plain'))

##p = MIMEBase('application', 'octet-stream')
##p.set_payload()

text = message.as_string()
server.sendmail(email, to_mail, text)
server.quit()

print('sended')
