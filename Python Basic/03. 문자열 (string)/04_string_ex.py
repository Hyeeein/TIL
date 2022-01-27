## 연습문제 1 : 입력된 문자열에서 알파벳, 숫자, 스페이스, 그 이외의 것에 대한 갯수를 각각 계산하여 출력
# 예) 문장을 입력하세요: 내 이름은 hyein이고, 내 메일은 phi498@naver.com 입니다.

string = input('문장을 입력하세요 : ')

strr = 0
num = 0
space = 0
etc = 0

for c in string:
    # 문자인 경우
    if c.isalpha():
        strr += 1
    # 숫자인 경우
    elif c.isdigit():
        num += 1
    # 스페이스인 경우
    elif c.isspace():
        space += 1
    # 그 외의 것인 경우
    else:
        etc += 1

print('문자의 갯수 : ', strr)
print('숫자의 갯수 : ', num)
print('공백의 갯수 : ', space)
print('기타의 갯수 : ', etc)

