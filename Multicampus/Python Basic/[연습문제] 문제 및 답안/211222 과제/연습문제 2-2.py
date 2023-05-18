# 연습문제 2-2 (12월 22일 과제)
# 만든 날짜 : 2021-12-23
# 만든이 : 박혜인

# 문제 1
num = input('16진수 한 글자 입력 : ')
if '0' <= num <= '9' or 'A' <= num <= 'F' or 'a' <= num <= 'f':   # 16진수에는 소문자, 대문자 a~f 모두 포함함
    print('10진수 ==> ', int(num, 16))
else:
    print('16진수가 아닙니다')


# 문제 2
money = int(input('교환할 돈은 얼마? '))
ohman, man, ohchen, chen, ohback, back, ohship, ship = 0, 0, 0, 0, 0, 0, 0, 0
margin = 0  # margin을 따로 안 쓰고, money%=50000 이런식으로 계산해나가도 상관없음

ohman = money // 50000
margin = money - 50000 * ohman

man = margin // 10000
margin = margin - 10000 * man

ohchen = margin // 5000
margin = margin - 5000 * ohchen

chen = margin // 1000
margin = margin - 1000 * chen

ohback = margin // 500
margin = margin - 500 * ohback

back = margin // 100
margin = margin - 100 * back

ohship = margin // 50
margin = margin - 50 * ohship

ship = margin // 10
margin = margin - 10 * ship

print('50000원 {}장, 10000원 {}장, 5000원 {}장, 1000원 {}장'.format(ohman, man, ohchen, chen))
print('500원 {}개, 100원 {}개, 50원 {}개, 10원 {}개' .format(ohback, back, ohship, ship))
print('바꾸지 못한 돈 ==> {}원' .format(margin))


# 문제 3
from random import randint

A = randint(1, 6)
B = randint(1, 6)

print('A의 주사위 숫자는 %d 입니다.' % A)
print('B의 주사위 숫자는 %d 입니다.' % B)

if A > B:
    print('A가 이겼다.')
elif A == B:
    print('A와 B가 비겼다.')
elif A < B:
    print('B가 이겼다.')