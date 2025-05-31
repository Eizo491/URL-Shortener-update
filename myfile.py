# myfile.py

from datetime import datetime

clicks = []

def track_click(short_url):
    timestamp = datetime.now().isoformat()
    clicks.append((short_url, timestamp))
    print(f"Tracked click on {short_url} at {timestamp}")

if __name__ == "__main__":
    short = input("Enter short URL to simulate click: ")
    track_click(short)
