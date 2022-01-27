## 날짜, 시간 형식 데이터 포맷

from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today.month
day = today.day
print(f'연도 : {year}, 월 : {month}, 일 : {day}')
print('연도 : {}, 월 : {}, 일 : {}' .format(year, month, day))

# print(datetime.today())
print(datetime.now().time())
current_time = datetime.now()
time = datetime.now().time().hour
minute = datetime.now().time().minute
second = datetime.now().time().second
microsec = datetime.now().time().microsecond


## 날짜 계산 : timedelta() 함수 사용
print(today + timedelta(days=-1))    # 여기서 +는 특정 날짜 추가
print(today + timedelta(days=1))
print(today + timedelta(days=-7))
print(today + timedelta(days=7))

current_time = datetime.now()
print(current_time + timedelta(hours=-1))
print(current_time + timedelta(days=1, hours=2))


## strftime () 함수 : 날짜 형식을 문자열로 반환
# H : 24시간,
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%Y-%m-%d %I:%M:%S %p'))

print(type(today))
print(type(current_time))


## strptime() 함수 : 문자열을 날짜형식으로 반환
today = '2020-06-20 17:40:20'
transToday = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
print(transToday)
print(type(transToday))