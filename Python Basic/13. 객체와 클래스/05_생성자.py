# 생성자 (construtor) : 인스턴스 생성 / 필드값을 초기화 함수

# 생성자의 형식
# class 클래스명:
#     def __init__(self, *args):
#         # 이 부분에 필드 초기화 코드 입력

# self : 클래스에서 생성된 인스턴스에 접근 (인스턴스 자신)
#        인스턴스가 생성된 후 해당 인스턴스 이름으로 값을 할당하거나 메소드 호출
#        클래스 내에서 self 호출
#        생성된 인스턴스 이름과 클래스 내의 self가 같은 역할을 함
#        메소드를 호출할 떄도 인스턴스의 이름과 메소드명을 사용

# 참고
# _ : 변수에 특별한 이름을 부여하지 않고 사용하려고 할 때

# for _ in range(10):
#     print('Hello')

# _ 2개 사용 : 특수한 예약함수(메소드), 변수에 사용

# if __init__ == '__main__' :

# 기본 생성자 : 생성자에 self만 있고, 다른 매개변수가 없음
# class 클래스명:
#     def __init__(self):
#         pass

class Car:
    def __init(self):
        self.speed = 0
        self.color = 'red'

car1 = Car()
print(f'자동차의 색상은 {car1.color}')
print(f'현재 자동차 속도는 {car1.spped}')

# 매개변수가 있는 생성자
# class 클래스명:
#     def __init__(self, *args):
#         pass

class Car1:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

# myCar = Car1() : 인수를 지정하지 않아서 TypeError 오류 발생
myCar = Car1(0, 'white')
print(isinstance(myCar, Car1))
print(f'myCar의 색상은 {myCar.color}')
print(f'myCar 속도는 {myCar.speed}')

# 디폴트 매개변수를 사용하는 생성자
# class 클래스명:
#     def __init__(self, arg1 = value1, arg2 = value3):
#         pass

class Car2:
    def __init__(self, speed = 0, color = 'red'):
        self.speed = speed
        self.color = color

myCar2 = Car2()
yourCar = Car2(10, 'white')
myCar3 = Car2('red')

print(f'myCar2의 색상은 {myCar2.color}')
print(f'myCar2 속도는 {myCar2.speed}')
print(f'yourCar의 색상은 {yourCar.color}')
print(f'yourCar 속도는 {yourCar.speed}')
print(f'myCar3의 색상은 {myCar3.color}')
print(f'myCar3 속도는 {myCar3.speed}')

class Car3:
    def __init__(self, color='red', speed=0):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 50

    def speedUp(self):
        self.speed += 10

# if __init__ = '__main__':
#     myCar4 = Car3()
#     print('초기 속도', myCar4.speed)
#     myCar4.drive()
#     print('drive() 수행 후 속도', myCar4.speed)
#     myCar4.speedUp()
#     print('speedUp() 수행 후 속도', myCar4.speed)

# 내 파일을 내가 실행하면 main / 아니면 참조하고 있는 상태
