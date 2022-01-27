# 1. 클래스 선언
# 클래스 이름 : 대문자로 시작,
#             식별자 규칙에 정의 (숫자가 먼저 나오면 안되고, 숫자 영문 혼용 가능, ...)
class Car:
    speed = 0
    color = ''

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        pass

# self : 인스턴스가 사용하는 것 (자신) / 기존의 함수와 구분

# 2. 객체(인스턴스) 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용

print(myCar.color)
myCar.color = 'black'
print(myCar.color)

# 메서드 호출 : 인스턴스.메서드()
myCar.speedUp()
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)

for i in range(3):
    try: print(i, 3// i)
    except ZeroDivisionError: print("Not divided by 0")