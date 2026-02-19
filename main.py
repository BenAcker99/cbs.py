import requests
import os

# הכתובת לבדיקה
URL = "https://www.cbs.gov.il/he/publications/DocLib/2026/yarhon0226/b2.pdf"

# קבלת המפתחות מגיטהאב
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram(text):
    if not TOKEN or not CHAT_ID:
        print("Error: Missing Telegram secrets.")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": text})
        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send message: {e}")

def check_site():
    print(f"Checking {URL}...")
    # דפדפן מדומה כדי לא להיחסם
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # בדיקה מהירה (HEAD)
        response = requests.head(URL, headers=headers, allow_redirects=True, timeout=10)
        
        if response.status_code == 200:
            print("File exists!")
            send_telegram(f"🚀 הקובץ פורסם!\n{URL}")
        else:
            print(f"Not found yet (Status: {response.status_code})")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_site()
