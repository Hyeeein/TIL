# 앞에서 작성한 Car 클래스에서 다음의 두 가지 메소드를 추가하시오

class Car:
    def __init__(self, modelN, speed = 0, color = 'white'):
        self.modelN = modelN
        self.speed = speed
        self.__color        # 클래스 내에서만 사용하는 비공개 필드

    def __modelN(self):
        print(self.modelN)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def printInfo(self):
        self.__modelN()
        print(self.getColor())

    # 여기부터 추가된 코드
    def speedUp(self, value):
        if self.speed >= 140:
            print('과속입니다. 속도를 줄이세요!')
            return self.speed
        else:
            self.speed += value

    def speedDown(self, value):
        if self.speed > 0:
            self.speed -= value
        else:
            self.speed = 0
            print('정지했습니다!')
