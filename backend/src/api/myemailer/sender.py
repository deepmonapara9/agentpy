from email.message import EmailMessage
import os
import smtplib

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT') or 465

# Here i am sending mail using gmail and i'm sending to myself and getting myself as the sender
def send_mail(subject: str = "No subject provided", content: str = "No message provided", to_email: str = EMAIL_ADDRESS, from_email: str = EMAIL_ADDRESS):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(content)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return smtp.send_message(msg)