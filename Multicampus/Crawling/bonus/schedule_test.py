from datetime import datetime
import schedule
import time

def job():
    now = datetime.now()
    print(now)

# 매 분마다 해당 작업을 실행
schedule.every().minutes.do(job)

# 매 시간마다 해당 작업을 실행
schedule.every().hour.do(job)

schedule.every().day.at('17:41').do(job)

schedule.every().monday.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# 1분에 1번씩 실행할 것