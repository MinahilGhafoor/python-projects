import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import logging
######################################################

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

logging.basicConfig(
    filename="logs\email.log",
    level= logging.INFO,
    format = "%(asctime)s - %(message)s"
)
###############################################
def send_email(TO, subject, body):

    for to in TO:
        to = to.strip()
        msg = MIMEMultipart()
        msg["FROM"], msg["TO"], msg["SUBJECT"] = EMAIL, to, subject
        msg.attach(MIMEText(body, "plain"))

        #======================================================
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            

            try:
                server.login(EMAIL, PASSWORD)
                server.send_message(msg)
                print(f"✅ Email sent to {to}")
                logging.info(f"✅ Success :   Subject: {subject}  Recipient: {to}")

            except smtplib.SMTPAuthenticationError:
                print("❌ Login failed — check your email and app password")
                logging.error("❌ Error: Login failed")
            except smtplib.SMTPException as e:
                print(f"❌ Email failed: {e}")
                logging.error(f"❌ Error: {e}")

        #======================================================

###############################################
def main():
    to = list(input("SEnd Email to:  ").split(','))
    subject = input("Subject: ")
    body = input("Body: ")
    send_email(to, subject, body)

main()