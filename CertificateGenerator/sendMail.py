import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import config as con

FROM = con.MAIL


def sendMail(name, toaddr):
    # instance of MIMEMultipart
    filename = name.replace(" ", "_").lower()+'.pdf'
    file_path = f"output/{filename}"

    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = FROM
    # storing the receivers email address
    msg['To'] = toaddr

    msg['Subject'] = con.SUBJECT

    body = con.body(name)
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(file_path, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', f"attachment; filename= {filename}")

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(FROM, con.PASS)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(FROM, toaddr, text)

    print(f"Mail Sent to {name} : {toaddr}\n")

    # terminating the session
    s.quit()
