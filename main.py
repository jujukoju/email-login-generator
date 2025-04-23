import smtplib
import uuid
from email.message import EmailMessage

email = input("Hi! What's your email? ")
user_name = email.lower().split("@")[0]
sender = "your_email_address"
app_password = "your_app_password"

# Credential Creation
username = f"{user_name}{uuid.uuid4().hex[:4]}"
password = uuid.uuid4()
text = (f"Here is your username: {username}\n"
        f"Here is your password: {password}\n" 
        "Happy logging in!🧑🏽‍💻")

msg = EmailMessage()
msg["Subject"] = "Login Details"
msg["From"] = sender
msg["To"] = email
msg.set_content(text)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
  
