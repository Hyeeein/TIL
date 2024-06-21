# 연습문제 3 (12월 22일 과제)
# 만든 날짜 : 2021-12-23
# 만든이 : 박혜인

# 문제 1 (1)
for i in range(5):
    num = 5 - i
    print('*' * num)

# 문제 1 (2)
for i in range(5):
    for j in range(9):
        space = 4 - i
        star = 9 - 2 * space
    print(' ' * space, '*' * star, ' ' * space, sep = '')
    # 구분자 ,의 디폴트값은 공백 하나 => seperator(구분자)를 뒤에 넣어 공백을 없애준다. sep = ''


# 문제 2
num = int(input('숫자 입력: '))

while True:
    if num == 7:
        break;
    num = int(input('다시 입력: '))

print('7 입력 ! 종료')


# 문제 3
sing = 0     # 부른 노래 곡 수
cost = 2000  # 노래방 비용

while True:
    sing += 1
    money = 10000 - sing*cost   # 잔액
    print('노래를 {}곡 불렀습니다.' .format(sing))
    if money == 0:
        break;
    print('현재 {}원 남았습니다.' .format(money))

print('잔액이 없습니다. 종료합니다.')