# 디폴트 매개변수
# 매개변수의 기본값을 지정

# def greet(name, msg):
#     print(name +'! '+ msg)

# def greet(name, msg='안녕^^'):
#     print(name +'! '+ msg)

# 디폴트 매개변수는 마지막에 위치해야 함
# def greet(msg='안녕^^', name):
#     print(name +'! '+ msg)

def greet(name='무명', msg='안녕^^'):
    print(name +'! '+ msg)

greet('홍길동','반가워')
greet('강감찬')
greet()

def showInfo(name, year=1, age=20):
    print(name, year, age)

showInfo('홍길동', 3 , 10)
showInfo('홍길동', 3)
showInfo('홍길동')

print('hi',end='#')
