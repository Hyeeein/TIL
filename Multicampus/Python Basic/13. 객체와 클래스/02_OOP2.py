# 클래스 구현과정
# 1단계 : 클래스 정의 (선언)
# class 클래스명:
#     필드1 = 0
#     필드2 = ''
#
#     def __init__(self):
#         self.필드명1 = 초기값
#         self.필드명2 = 초기값
#
#     def 메소드명1 (self, 매개변수, ...):
#         pass
#
#     # 메소드 정의는 함수를 정의하는 것과 동일

# 2단계 : 객체 생성 (인스턴스 생성), 변수 선언과 비슷
# 객체변수명 = 클래스명()

# 3단계 : 객체 이용, 메소드 호출, 필드값 변경, 필드값 사용
# 변수나 함수와 다르게 구별하기 위해서
# 객체이름.변수명
# 객체이름.메소드명


# 자동차 클래스
# 기능(동작) => 메소드 (함수) : speedUp(), speedDown()
# 속성(상태, 값) => 변수(필드) : color, speed

# 1. 클래스 선언
# 클래스 이름 : 대문자로 시작,
#             식별자 규칙에 정의 (숫자가 먼저 나오면 안되고, 숫자 영문 혼용 가능, ...)
class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

    def speedUp(self):
        pass

    def speedDown(self):
        pass

# 2. 객체(인스턴스) 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
myCar.speedUp()
print(myCar.color)
myCar.color = 'black'
print(myCar.speed)

# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
print(isinstance(myCar, Car))

# 파이썬에서 기본적으로 제공하는 함수들
# int, list, range, dict, str, ...

a = int(10)
print(type(a))

b = list(range(10))
print(type(b))

c = dict(X = 10, y = 20)
print(type(c))

d = str(10)
print(type(e))

# 객체와 인스턴스
# 객체 : 객체만 지칭할 때는 객체 (object) 라고 하고
# 인스턴스 : 클래스와 연관지어서 부를 때 사용