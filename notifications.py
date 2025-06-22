import config
import smtplib
from email.message import EmailMessage

def send_alert(message):
    print(f"[ALERT] {message}")
    if config.EMAIL_ENABLED:
        try:
            msg = EmailMessage()
            msg.set_content(f"Security Alert: {message}")
            msg['Subject'] = "Vehicle Security Alert"
            msg['From'] = config.EMAIL_USERNAME
            msg['To'] = config.EMAIL_TO
            with smtplib.SMTP(config.EMAIL_SMTP_SERVER, config.EMAIL_SMTP_PORT) as server:
                server.starttls()
                server.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print("[Email Error]", e)
