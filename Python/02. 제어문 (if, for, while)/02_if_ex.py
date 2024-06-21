# if문 연습문제 (12월 22일 수요일)

## 연습문제 1 : 정수 3개를 입력 받아서 제일 큰 수를 출력하기

num1 = int(input('정수 1 입력: '))
num2 = int(input('정수 2 입력: '))
num3 = int(input('정수 3 입력: '))

if num1 >= num2 and num1 >= num3:
    print('제일 큰 수: %d' % num1)
elif num2 >= num3:  # num2 >= num1은 이미 앞에서 걸러진 거니까 굳이 쓰지 않음
    print('제일 큰 수: %d' % num2)
else:
    print('제일 큰 수: %d' % num3)


## 연습문제 2 : 도형을 선택해서 면적 구하기

sel = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원): '))

if sel == 1:
    width = int(input('가로 입력: '))
    height = int(input('세로 입력: '))
    area = width * height
    print('사각형의 면적 = %.2f' % area)

elif sel == 2:
    width = int(input('밑변 입력: '))
    height = int(input('높이 입력: '))
    area = 1/2 * width * height
    print('삼각형의 면적 = %.2f' % area)

elif sel == 3:
    radius = int(input('반지름 입력: '))
    PI = 3.141592
    area = PI * radius * radius
    print('원의 면적 = %.2f' % area)

else:
    print('잘못 입력하셨습니다.')