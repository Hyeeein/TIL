# 상수

# 값이 변하지 않음.
# 변수와 구분하기 위해 대문자로 사용
# 나중에 값을 바꿀 수 있음 (오류 없음). 하지만 보통은 상수로 사용

PI = 3.141592

# 예: 원의 둘레와 면적 계산해보기

radius = 10
area = radius * radius * PI

print(area)

# 예: 이자 계산

RATE = 0.03
deposit = 100000
interest = deposit * RATE
balance = deposit + interest

print(int(balance))
print(format(balance, ','))  # 천 단위 구분자