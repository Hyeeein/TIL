# in / not in
# 문자열 내에 특정한 문자열이 포함되어 있는지 확인
# 결과 : True, False

string = 'Python programming'
result = 'on' in string
# result = 'on' not in string

print(result)  # on 글자가 있으면 True, 없으면 False


## 예제 1 : in 활용
ID = input('ID 입력 : ')
ids = ['sun', 'hipark', 'moon', 'sky']

if ID in ids:
    print('로그인 성공')
else:
    print('로그인 실패')
