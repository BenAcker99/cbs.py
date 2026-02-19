import requests
import os
import sys

# הכתובת לבדיקה
URL = "https://www.cbs.gov.il/he/publications/DocLib/2026/yarhon0226/b2.pdf"

# קבלת המפתחות משתני הסביבה (נגדיר אותם בגיטהאב)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(send_url, data=data)
        print("Telegram message sent.")
    except Exception as e:
        print(f"Error sending message: {e}")

def check_file():
    print(f"Checking URL: {URL}")
    
    # שימוש ב-User-Agent כדי שהשרת לא יחסום את הבוט
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # שליחת בקשת HEAD לבדיקת קיום הקובץ
        response = requests.head(URL, headers=headers, allow_redirects=True, timeout=10)
        
        # קוד 200 אומר שהקובץ קיים ותקין
        if response.status_code == 200:
            print("File found! Sending notification...")
            msg = f"🚀 הקובץ מהלמ''ס נמצא!\nהנה הקישור: {URL}"
            send_telegram_message(msg)
        else:
            print(f"File not found yet. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"Error checking URL: {e}")

if __name__ == "__main__":
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: Missing Telegram secrets.")
        sys.exit(1)
    
    check_file()
