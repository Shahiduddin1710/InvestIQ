import os
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter, HTTPException
from schemas import ContactRequest

router = APIRouter(prefix="/contact", tags=["contact"])

EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")


@router.post("")
async def send_contact(req: ContactRequest):
    if not req.name or not req.email or not req.message:
        raise HTTPException(status_code=400, detail="All fields are required")

    if not EMAIL_RE.match(req.email):
        raise HTTPException(status_code=400, detail="Invalid email address")

    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    receiver = os.getenv("CONTACT_RECEIVER", smtp_user)

    if not smtp_user or not smtp_pass:
        raise HTTPException(status_code=500, detail="Email not configured on server")

    msg = MIMEMultipart()
    msg["From"] = f"InvestIQ Contact <{smtp_user}>"
    msg["To"] = receiver
    msg["Reply-To"] = req.email
    msg["Subject"] = "New Contact Message - InvestIQ"

    body = f"""New message received from InvestIQ Contact Form

Name: {req.name}
Email: {req.email}

Message:
{req.message}
"""
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, receiver, msg.as_string())
        server.quit()
        return {"success": True, "message": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
