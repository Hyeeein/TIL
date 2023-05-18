# 문자열에서 사용되는 연산 함수(메소드)들

# len() : 문자열 길이 반환
string = 'programming'
print(len(string))

# .count() : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print(string.count('r'))
print(string.count('m'))
print(string.count('ing'))

# .find(찾을 문자[, start [, end]]) -> 여기서 []는 써도 되고 안써도 된다는 의미
# 문자열 내에서 특정 문자(열)이 존재하면 문자열의 시작 위치를 반환하고, 존재하지 않으면 -1을 반환

crawling = 'Data crawling is fun'
print(crawling.find('is'))       # 찾으면 인덱스 반환
print(crawling.find('parsing'))  # 찾는 문자열이 없는 경우 -1을 반환
print(crawling.find('is', 15))
print(crawling.find('is', 5, 10))

# .index(찾을 문자[, start [, end]])
# 문자열 내에서 특정 문자열의 시작 위치를 반환, 찾는 문자열이 없으면 에러를 반환

print(crawling.find('is'))       # 찾으면 인덱스 반환
print(crawling.find('parsing'))  # 찾는 문자열이 없는 경우 ValueError
print(crawling.find('is', 15))
print(crawling.find('is', 5, 10))


## 연습문제 1 : 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기

cities = '인천 대구 대전 부산 울산 청주 춘천'
name = input('도시명을 입력하시오 : ')

# in을 이용할 경우
if name in cities:
    print('해당 도시가 있습니다.')
else:
    print('해당 도시는 없습니다.')

# find()를 이용할 경우
if cities.find(name) != -1:
    print('정답')
else:
    print('오답')