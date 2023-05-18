# for 문 연습문제

## 연습문제 1 : 9, 7, 5, 3, 1로 줄어드려면 range를 어떻게 써야하나?
for number in range(9, 0, -2):
    print(number)


## 연습문제 2 : 1부터 10까지 더하기

# = : 할당연산자
# 대입연산자 : +=, -=, *=, /=
# x += 1 : x = x + 1 누적 더하기
# x -= 1 : x = x - 1

result = 0
for i in range(1, 11):
    result += i
print(result)


## 연습문제 3 : 1~100까지의 홀수만 더한 결과 출력

result = 0
for i in range(1, 101, 2):
    result += i
print(result)


## 연습문제 4 : 1~100 사이 정수 중 홀수와 짝수의 합을 각각 구하여 출력

odd = 0
even = 0

for i in range(1, 101):
    if i % 2 == 1:
        odd += i
    else:
        even += i

print('홀수의 합은', odd)
print('짝수의 합은', even)


## 연습문제 5 : 1~100 사이의 3의 배수를 출력하고 더하기

result = 0

for i in range(3, 100, 3):
    print(i)
    result += i
print('3의 배수의 합은', result)


## 연습문제 6 : 구구단의 단수를 입력받아서 구구단을 출력하기

num = int(input('단수 입력 : '))

for i in range(1, 10):
    result = num * i
    print('{} * {} = {}' .format(num, i, result))
    # print(num, "*", i, "=", result)
    # print(num, "*", i, "=", num * i)
    # print('%d * %d = %d', % (num, i, num * i))
    # 참고: 내가 쓴 코드 중괄호 3번째거에 :2d를 넣어주면 줄맞춤 되어서 출력할 수도 있음


## 연습문제 7 : 카운트 다운 프로그램 (시작 숫자를 입력하면 숫자가 하나씩 줄어들면서 출력하는 것)
# 출력 화면 : 10 9 8 7 6 5 4 3 2 1 성공

num = int(input('시작 숫자를 입력하시오 : '))

for i in range(num, 0, -1):
    print(i, end = ' ')
    if i == 1:
        print('성공')

# 예시 답안
# num = int(input('시작 숫자를 입력하시오 : '))
#
# for i in range(num, 0, -1):
#     print(i, end = ' ')
# print('성공')


## 연습문제 8 : for에서 리스트를 이용
# 학생 성적 리스트 score = [70, 90, 100, 50, 85]
# 60점 이상 합격, 60미만은 불합격 출력
# 1번 학생 합격
# 2번 학생 합격
...
# 5번 학생 합격

score = [70, 90, 100, 50, 85]
count = 0

for i in score:
    count += 1
    if i >= 60:
        print('%d번 학생: 합격' % count)
    else:
        print('%d번 학생: 불합격' % count)


## 연습문제 9 : 숫자 10개를 입력 받아서 양, 음, 0의 개수 출력

plus = 0
minus = 0
zero = 0

for i in range(1, 11):
    num = int(input('숫자 %d 입력 : ' % i))

    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    elif num == 0:
        zero += 1

print('---------------')
print('양의 개수 : %d' % plus)
print('음의 개수 : %d' % minus)
print('0의 개수 : %d' % zero)


## 연습문제 10 : 리스트에 있는 이름인지 확인

names = ['베토벤', '홍길동', '변화도', '아쿠아맨']
search_name = input('이름 입력: ')

for name in names:
    if search_name == name:
        find = True
        break
    else:
        find = False

if find:
    print('명단에 있어요')
else:
    print('명단에 없어요')