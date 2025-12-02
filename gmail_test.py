from google.auth.transport.requests import Request
from google.auth import default
from googleapiclient.discovery import build

# Ambil credentials dari environment (WIF via GitHub Actions)
credentials, project_id = default(scopes=["https://www.googleapis.com/auth/gmail.readonly"])

# Buat Gmail API client
service = build("gmail", "v1", credentials=credentials)

# Contoh: list 10 pesan pertama
results = service.users().messages().list(userId="me", maxResults=10).execute()
messages = results.get("messages", [])

if not messages:
    print("No messages found.")
else:
    for msg in messages:
        print(f"Message ID: {msg['id']}")
