import smtplib
from email.message import EmailMessage

SENDER_EMAIL ="meghaneethimani@gmail.com"
APP_PASSWORD = "vwrywagghkbdfpon"
RECEIVER_EMAIL = "meghaneethimani@gmail.com"
def send_email(report):

    msg = EmailMessage()
    msg["Subject"] = "CRITICAL SYSTEM ALERT"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    body = f"""
{report["summary"]}

Root Causes:
- {"\n- ".join(report["root_causes"])}

Error Types:
- {"\n- ".join(report["error_types"])}

Recommended Action:
{report["action"]}

Resolution Status: Automatic resolution not possible
Severity: CRITICAL
Escalation Required: YES
Assigned Team: Infrastructure / DevOps
"""

    msg.set_content(body)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()