# if문

## 연습문제 1 : id와 password를 입력 받아 모두 맞으면 로그인 성공 출력, 그렇지 않으면 로그인 실패 출력

id = input('아이디를 입력해주세요: ')
pw = input('비밀번호를 입력해주세요: ')

if id == 'multicampus' and pw == '1234' :
    print('로그인 성공')
else :
    print('로그인 실패')


# 중첩 if
if id == 'multicampus' :
    if pw == '1234' :
        print('로그인 성공')
    else :
        print('비밀번호가 다릅니다')

if num > 0:
    print('양수')
else:
    if num == 0:
        print('0')
    else:
        print('음수')

# if~ elif
if num > 0:
    print('양수')
elif num == 0:
    print('0')
else:
    print('음수')


## 연습문제 2 : 정수를 입력 받아서 홀수인지 짝수인지 판별하여 출력

num = int(input('정수 입력: '))
if num % 2 == 0 :
    print('짝수')
else :
    print('홀수')


## 연습문제 3 : 점수를 입력받아서 학점 출력 A, B, C, D, F

score = float(input('점수를 입력해주세요: '))
if score >= 90 and score <= 100:
    print('A')
elif 80<= score < 90:
    print('B')
elif 70<= score < 80:
    print('C')
elif 60<= score < 70:
    print('D')
else:
    print('F')