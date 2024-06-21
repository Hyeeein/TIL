# 문자열 슬라이싱 (slicing) : 연산자를 사용한다

crawling = 'Data crawling is fun.'
parsing = 'Data parsing is also fun.'

print(crawling)
print(crawling[0])   # 첫 번째 문자
print(crawling[-1])  # 마지막 문자

# 슬라이싱 예시
print(crawling[0:4]) # 0~3번째 까지의 문자들
print(crawling[17:]) # 17번째 문자부터 끝까지
print(crawling[:18])
print(crawling[-1:]) # 마지막에서 끝까지
print(crawling[:-1]) # 처음부터 마지막 전까지
print(crawling[10:10+5])
print(parsing[:])    # 전체 다 가져오는 것


# 문자열 결합 : join()
# 각 문자 사이에 특정문자(열) 삽입

a = 'aa'
print(a.join('bbb'))

a = ','
print(a.join('1234'))


# 문자열 변경 : replace(찾는 문자열, 변경할 문자열)
# 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경
# 찾는 문자열이 존재하면 변경할 문자열로 대체하여 반환
# 찾는 문자열이 없는 경우 원래 문자열을 반환

lan = 'Python programming'
print(lan.replace('Python', 'Java'))
print(lan.replace('on', 'om'))
print(lan.replace('oq', 'om'))


# 대소문자 변경
# upper() : 대문자로 변경
# lower() : 소문자로 변경
# capitalize() : 문장의 첫 번째 문자열의 첫 문자를 대문자로 변환
# title() : 각 단어의 첫 문자를 대문자로 변경
# swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경

lan = 'python programming'
print(lan.upper())
print(lan.lower())
print(lan.capitalize())
print(lan.swapcase())
print(lan.title())


# 공백제거
# strip() : 문자열의 앞뒤의 공백을 제거
# lstrip() : 문자열의 왼쪽의 공백을 제거
# rstrip() : 문자열의 오른쪽 공백을 제거

string = '  python  '
print(string.strip())
print(string.lstrip())
print(string.rstrip())


## 문자열 구성 파악
# isalpha() : 문자 여부 결과 반환 (True, False)
# isdigit() : 숫자인지 결과 반환
# isspace() : 하나의 문자에 대하여 공백여부 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자여부
# isupper() : 대문자여부

string = '내 이름은 hyein이고, 나이는 22입니다'
str_split = string.split()
for result in str_split:
    if result.isalpha():
        print('숫자군요!')
    else:
        print('숫자가 아니에요')

