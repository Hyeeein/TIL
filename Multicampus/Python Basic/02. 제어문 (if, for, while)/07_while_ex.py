# while 문 연습문제

## 연습문제 1 : 'stop' 문자 입력될 때까지 숫자를 입력하고, 입력된 숫자의 개수를 출력

num = input('숫자 입력 : ')
count = 0

while num != 'stop' :
    num = int(num)
    count += 1
    num = input('숫자 입력 : ')
    print(num)
print('숫자 갯수 : ' , count)


## 연습문제 2 : 7을 입력할 때까지 계속 입력하기. 7이 입력되면 프로그램 종료

num = int(input('숫자 입력 : '))
while num != 7:
    num = int(input('숫자 입력 : '))
print(num, '입력! 종료')


## 연습문제 3 : 'q'가 입력되면 종료

while True:
    inp = input('종료하려면 q입력 : ')
    if inp == 'q':
        break

print('입력! 종료')
