# 반환값이 1개인 경우

# 문제1. 사각형의 넓이 계산하는 함수 getArea()
# 매개변수(parameter) : 가로(width), 세로(height)
# 넓이를 반환


# def getArea(width, height):
#     result = width*height
#     return result
# def getArea(width, height):
#     return width*height
#
# print(getArea(10, 20))

# 문제2. 사각형의 넓이 계산하는 함수 getArea()
# 가로와 세로의 길이를 입력받기
# 넓이를 반환

def getArea():
    width = int(input('가로 : '))
    height = int(input('세로 : '))
    result = width * height
    print(f'가로: {width}, 세로: {height}, 사각형넓이={result}')
    return result

# result = getArea()


# 반환값이 여러 개인 경우
# def multi_return():
#     return 1, 2, 3

# # 반환된 여러개의 값을 하나의 변수에 받기
# result = multi_return()
# print(result)
# print(type(result))  # 튜플 형식으로
#
# # 반환된 여러 개의 값을 여러 변수로 각각 받기
# a, b, c = multi_return()
# print(a,b,c)

# return 문이 여러개 사용할 경우 : 가장 첫번째 return 문장만 실행
# return : 값을 반환하고 함수 종료

def multi_return():
    return 1
    return 2
    return 3

result= multi_return()
print(result)