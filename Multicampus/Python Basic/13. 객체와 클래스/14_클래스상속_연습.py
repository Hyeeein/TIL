# 클래스 상속과 메소드 재정의 연습

# Animal 클래스 정의
# 메소드 : talk(), eat(), sleep()
# 필드 : age, leg, color, breed

# 서브클래스 Dog 클래스
# 메소드 : talk() 재정의 -> '멍멍'

# 서브클래스 Cat 클래스
# 메소드 : talk() 재정의 -> '야옹'

# 서브클래스 Rabbit 클래스
# 메소드 : talk() 재정의 -> '깡총'

class Animal:
    age = 0
    leg = 4
    color = ''
    breed = ''

    def __init__(self, age, leg, color, breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def talk(self):
        print('짓는다')

    def eat(self):
        print('먹는다')

    def sleep(self):
        print('잔다')

# 서브클래스 Dog()
class Dog(Animal):
    def talk(self):
        print('멍멍')

# 서브클래스 Cat()
class Cat(Animal):
    def talk(self):
        print('야옹')

# 서브클래스 Rabbit()
class Rabbit(Animal):
    def talk(self):
        print('깡총깡총')


# dog1 = Dog()
# cat1 = Cat()
# rabbit = Rabbit()
# dog1.talk()
# cat1.talk()
# rabbit.talk()


# 다형성 (polymorphism) : 같은 이름의 메소드가 다른 기능을 할 수 있도록 하는 것
animals = [Dog(1, 4, 'white', 'A'), Cat(1, 4, 'Red', 'B'), Rabbit(2, 4, 'black', 'C')]

for animal in animals:
    animal.talk()
