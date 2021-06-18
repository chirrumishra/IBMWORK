import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_user = 'oprojecttrial@gmail.com'
smtp_password = 'disasterMANAGEMENT!@#$'
server = 'smtp.gmail.com'
port = 587
msg = MIMEMultipart("alternative")
msg["Subject"] = '!!!!!!STORM ALERT!!!!!!'
msg["From"] = smtp_user
msg["To"] = "oprojecttrial@gmail.com"
msg.attach(MIMEText('\nsent via python', 'plain'))
s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.login(smtp_user, smtp_password)
s.sendmail(smtp_user, "oprojecttrial@gmail.com", msg.as_string())
s.quit()