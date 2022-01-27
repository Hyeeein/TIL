# 필드 이용 메소드

class Car:
    model = ''

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    # 필드값을 반환하는 메소드
    def getModel(self):
        return self.model

    # 필드값을 지정하는 메소드
    def setModel(self, model):
        self.model = model

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

myCar = Car(0, 'red', '아우디')
print(myCar.getColor())
myCar.setModel('벤츠')
print(myCar.getModel())