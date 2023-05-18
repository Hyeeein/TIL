# while 문 : 정해진 조건에 따라 반복문을 수행

# 초기값
# while 조건:
#     반복문장 1
#     반복문장 2
#     ...
#     증감

# 1부터 10까지 출력
for i in range(1, 11):
    print(i, end = ' ')
print('\n ----------')

i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# 1 ~ 10 까지 더하기
i = 1
sumN = 0
while i<=10:
    sumN += i
    i += 1
print(sumN)

# ----------

# while & break : 무한루프 이용

while True:
    num = int(input('숫자입력 : '))
    if num == 7:    # 7이 입력되면 종료
        break

print(num, '입력! 종료')

while 1:
    num = int(input('숫자입력 : '))
    if num == 7:
        break

print(num, '입력! 종료')