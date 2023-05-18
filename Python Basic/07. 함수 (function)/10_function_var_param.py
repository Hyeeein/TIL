# 가변길이 매개변수 : *args,  **kwargs
# 매개변수의 개수가 정해져 있지 않은 경우
# 여러 개의 값을 전달받아 사용할 경우
# *args : arguments의 약자, 인수 값을 받음
# **kwargs : keyWord arguments 의 약자, key=value 값을 받음

# 예제1. *args 형식을 이용하여 여러 개 인수의 값을 더하는 함수
def sumN(*args):
    total=0
    for x in args:
        total += x

    return total

# print(sumN(1,2,3))
# print(sumN(1,2,3,4,5))
# print(sumN(1,2,3,4,1,5,6,7,10))

# 예제2. *매개변수 형식을 사용하여
def showNames(*names):
    # result=''
    for name in names:
        print(name, end=' ')
        # result += name + ' '
    #return result
    print()

# showNames('홍길동','강감찬')
# showNames('홍길동','강감찬','유관순','이순신')


# **kwargs 예제 : 키=값
def showInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print('\n')
    for value in kwargs.values():
        print(value, end=' ')
    print('\n')
    for item in kwargs.items():
        print(item)

showInfo(name='홍길동', id='123', phone='010-111-111', address='서울시 서초구 삼성동')
showInfo(name='sun', id='moon')



