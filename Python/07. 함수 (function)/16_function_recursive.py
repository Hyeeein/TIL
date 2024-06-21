# 재귀 함수 : 자기함수 호출

# 문제1. 팩토리얼 계산
# 3! = 3*2*1  0!=1
# n! = n*(n-1)!
# (n-1)! = (n-1)*(n-2)!

# 반복문을 사용해서 구성
def factorial(n):
    fac=1
    for i in range(n,0, -1):
        fac *= i
    return fac

# fac(n) = n*fac(n-1)
# fac(n-1) = (n-1)*fac(n-2)
# fac(1) = 1
#
# fac(n) = n*(n-1)*(n-2)*...*1

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

# n=int(input('숫자입력: '))
# print(f'{n}! = {factorial(n)}')

# 5! =>  fact(5) -> 5*fact(4) -> 4*fact(3) -> 3*fact(2) -> 2*fact(1)  -> 1
# fact(5) <- 5*4*3*2*1 <- 4*3*2*1 <- 3*2*1 <- 2*1  <- 1

# 주의 : RecursionError: maximum recursion depth exceeded while calling a Python object
def selfCall():
    print('hello', end=' ')
    selfCall()

# selfCall()

# 문제2. 카운트다운
# 반복문 이용
def count(number):
    if number >=1:
        for n in range(number, 0, -1):
            print(n, end=' ')
        print()
    else:
        print('1이상인 숫자를 입력하세요')

# count(10)

# 재귀함수 이용
def selfCount(number):
    if number >= 1:
        print(number)
        selfCount(number-1)
    else:
        return

selfCount(5)