# 딕셔너리(dictionary) : 키와 값의 쌍으로 이루어진 데이터
# {키1:값1, 키2:값2, ...}

# 딕셔너리 생성 : {} 또는 dict()
students = {1:'최선', 2:'홍길동', 3:'강감찬'}
print(students)
print(type(students))

prof = {}
prof[1]='이순신'
prof[2]='홍길동'
print(prof)

print(students[1])

member = {'name':'홍길동', 'phone':'010-1234-1234'}
print(member)
print(member['name'])
# print(member['홍길동'])

member1 = {'name':'홍길동', 'phone':'010-1234-1234', 'name':'이순신'}
member1['name'] = '이순신'
print(member1)

naver = {'name':'naver', 'url':'www.naver.com', 'id':'hipark'}
google = {'name':'google', 'url':'www.google.com', 'id':'hipark'}
daum = {'name':'daum', 'url':'www.daum.net', 'id':'hipark'}

print(naver['name'])
naver['id'] = 'idValue'
print(naver['name'])


# key(), values(), items()
print(naver.keys())
print(naver.values())
print(naver.items())
for key in naver.keys():
    print(key)

print(type(naver.keys()))
to_list = list(naver.keys())
print(to_list)

for key in naver.keys():
    print(key)

for value in naver.values():
    print(value)

for item in naver.items():
    print(item)


# key로 value 찾기
print(naver['name'])
print(naver.get('name'))

# print(naver['passwd'])
print(naver.get('passwd', '없음'))
key = 'passwd'
if naver.get(key) is None:
    print(key + '에 대한 값이 없습니다')

print(key in naver)
print(key not in naver)

if key not in naver:
    print(key + '에 대한 값이 없습니다')

