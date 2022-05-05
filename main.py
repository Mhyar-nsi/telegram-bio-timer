from pyrogram import Client
import time 
import schedule
from datetime import datetime

api_id = # your telegram api id 
api_hash = "" # your telegram hash id

app = Client("bot" , api_id , api_hash)


def job():
    with app:
        tm = datetime.now().time().strftime('%H:%M')
        app.update_profile(bio=f"time : {tm}")

schedule.every().minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
