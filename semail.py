import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USERNAME = 'utpalpitest@gmail.com'
GMAIL_PASSWORD = 'xxxxxxx'

"""
This is the first version of sendEmail. It just sends an
email with body and subject.
"""
def sendEmail(body, subject=''):
    recipient = 'utpalchakraborty@gmail.com'
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                       "subject: " + subject,
                       "to: " + recipient,
                       "mime-version: 1.0",
                       "content-type: text/html"])

    # body_of_email can be plaintext or html!                    
    content = headers + "\r\n\r\n" + body
    session.sendmail(GMAIL_USERNAME, recipient, content)

"""
This is the second version of send email. This sends an email
with body and an optional list of attachments. 
"""
def sendEmail2(body, subject='', attachments = None):
    recipient = 'utpalchakraborty@gmail.com'
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = GMAIL_USERNAME
    msg['To'] = recipient
    msg.attach(MIMEText(body, 'plain'))

    if attachments != None:
        for f in attachments:
            fp = open(f, 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)
    
    session.sendmail(GMAIL_USERNAME, recipient, msg.as_string())
