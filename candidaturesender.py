import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


your_email = "email@test.com"
your_password = "abcd abcd abcd abcd"  
cv_path = "cv.pdf"
emails_file = "emails.txt"
sent_file = "sent.txt"
emails_per_hour = 30 # 30 emails send each 1800s
delay_between_batches = 1800  #delay between emails


subject = "Candidature pour un stage ..."

message_body = """
Madame, Monsieur,

Actuellement ...
[the body of the message here ]
"""


sent = set()
if os.path.exists(sent_file):
    with open(sent_file, "r") as f:
        sent = set(line.strip() for line in f if line.strip())


with open(emails_file, "r") as f:
    emails = [line.strip() for line in f if line.strip() and line.strip() not in sent]

print(f"Total remaining emails to send: {len(emails)}")


for i, recipient in enumerate(emails):
    print(f"Sending email to {recipient}...")

    msg = MIMEMultipart()
    msg["From"] = your_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "plain"))


    with open(cv_path, "rb") as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(cv_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(cv_path)}"'
        msg.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(your_email, your_password)
            server.send_message(msg)
        print(f"[✓] Sent to {recipient}")

        # Mark as sent
        with open(sent_file, "a") as f:
            f.write(recipient + "\n")

    except Exception as e:
        print(f"[x] Failed to send to {recipient}: {e}")


    if (i + 1) % emails_per_hour == 0 and (i + 1) != len(emails):
        print(f"Waiting 1 hour before sending the next {emails_per_hour} emails...")
        time.sleep(delay_between_batches)
