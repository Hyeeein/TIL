# 연습문제 4-3 (12월 23일 과제)
# 만든 날짜: 2021-12-23
# 만든이: 박혜인

heart = []
num = input('숫자를 여러개 입력하세요.')

for i in num:
    heart.append(int(i))

for i in heart:
    print('\u2665' * i)


## 예시답안
# heart = '\u2665'
# number = input('숫자 입력 : ')
# for n in number:
#     for i in range(int(n)):
#         print(heart, end='')
#     print()