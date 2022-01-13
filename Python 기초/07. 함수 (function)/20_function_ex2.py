# # 문제 1. 팩토리얼 계산
#
# def factorial(n):
#     sum = 1
#     for i in range(n, 0, -1):
#         sum *= i
#     return sum
#
# n = int(input('숫자 입력 : '))
# print(f'{n}! = {factorial(n)}')
#
# # 재귀함수를 이용하는 경우
#
# # n! = n*(n-1)!
# # (n-1)! = (n-1)*(n-2)!
#
# # fac(n) = n * fac(n-1)
# # fac(n-1) = (n-1) * fac(n-2)
# # fac(1) = 1
#
# # fac(n) = n * (n-1) * (n-2) * ... * 1
#
# def factorial(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)
#
# n = int(input('숫자 입력: '))
# print(f'{n}! = {factorial(n)}')


# 문제 2. 카운트다운

# for 반복문 이용
def count(number):
    for i in range(number, 0, -1):
        print(i)
count(5)

# 재귀함수 이용
def selfCount(number):
    if number == 0:
        return 0
    else:
        print(number)
        return selfCount(number - 1)
selfCount(5)



## 예시 답안 (카운트다운)

# 반복문 사용
def count(number):
    if number >= 1:
        for n in range(number, 0, -1):
            print(n, end = ' ')
        print()
    else:
        print('1이상인 숫자를 입력하세요.')

count(10)

# 재귀함수 사용
def selfCount(number):
    if number >= 1:
        print(number)
        selfCount(number - 1)
    else:
        return

selfCount(10)