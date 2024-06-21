# 산술연산 함수 작성
# add() : 더하기
# sub() : 빼기
# mul() : 곱하기
# div() : 나누기
# mod() : 나머지

# a=9, b=3
# 두 개의 숫자를 전달받아서 연산 결과 반환

# 9 + 3 = 12
# 9 - 3 = 6
# 9 * 3 = 27
# 9 / 3 = 3
# 9 % 3 = 0

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def mod(a, b):
    return a%b

a,b=9,3
# result =add(a,b)
# print(f'{a} + {b} = {result}')
# result =sub(a,b)
# print(f'{a} - {b} = {result}')
# result =mul(a,b)
# print(f'{a} * {b} = {result}')
# result =div(a,b)
# print(f'{a} / {b} = {result}')
# result =mod(a,b)
# print(f'{a} % {b} = {result}')
#

def printArithm(a,b):
    result =add(a,b)
    print(f'{a} + {b} = {result}')
    result =sub(a,b)
    print(f'{a} - {b} = {result}')
    result =mul(a,b)
    print(f'{a} * {b} = {result}')
    result =div(a,b)
    print(f'{a} / {b} = {result}')
    result =mod(a,b)
    print(f'{a} % {b} = {result}')

printArithm(10, 15)



