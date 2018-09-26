# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

textfile = 'foo.txt'

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = 'noreply@test.com'
msg['To'] = 'warren.wrate@test.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('##SMTP.com###',25)
s.send_message(msg)
s.quit()
