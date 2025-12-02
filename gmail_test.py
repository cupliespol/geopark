from email.mime.text import MIMEText
import base64
import google.auth
from googleapiclient.discovery import build

def create_message(sender, to, subject, message_text):
    """Bikin pesan MIME dan encode base64 untuk Gmail API"""
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    """Kirim pesan via Gmail API"""
    try:
        sent = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message Id: {sent['id']}")
        return sent
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Autentikasi otomatis via GitHub Actions WIF
    creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/gmail.send"])
    service = build('gmail', 'v1', credentials=creds)

    # Ganti alamat email sesuai service account / alias Gmail kamu
    sender = "geopark-sa@ornate-ensign-480013-s3.iam.gserviceaccount.com"
    to = "email.support@terrafirmaconsultantsllc.site"
    subject = "Test Email from GitHub Actions"
    body = "Halo bosku, ini email test dikirim via Gmail API + WIF 🚀"

    message = create_message(sender, to, subject, body)
    send_message(service, "me", message)

if __name__ == "__main__":
    main()
