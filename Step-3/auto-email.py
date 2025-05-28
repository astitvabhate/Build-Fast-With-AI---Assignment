
import pandas as pd
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file_path = 'email_and_message.csv' 
df = pd.read_csv(file_path)

# SMTP config
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

# Your email credentials
FROM_EMAIL = input("Enter your Gmail address: ")
PASSWORD = getpass.getpass("Enter your Gmail app password: ")

# Loop through and send emails
for index, row in df.iterrows():
    to_email = row['email']
    message_body = row['final_message']

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = "Thanks from Our Team!"
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, PASSWORD)
            server.send_message(msg)

        print(f"✅ Sent to: {to_email}")

    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")
