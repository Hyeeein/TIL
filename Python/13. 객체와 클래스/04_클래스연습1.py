# Dog 클래스와 인스턴스 만들기

class DOG():

    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
        print(f'Breed: {breed} / Size: {size} / Age: {age} / Color: {color}')

    def Eat(self):
        pass
    def Sleep(self):
        pass
    def Sit(self):
        pass
    def Run(self):
        pass

dog1 = DOG('Neapolitan Mastiff', 'Lage', '5 years', 'Black')
dog2 = DOG('Maltese', 'Small', '2 years', 'White')
dog3 = DOG('Chow Chow', 'Midium', '3 years', 'Brown')

# ----------------- #
### 강사님 예시 답안 ###

class Dog:

    breed = ''
    size = ''
    age = 0
    color = 'white'

    # def __init__(self):
    #     self.breed = ''
    #     self.size = ''
    #     self.age = ''
    #     self.color = 'white'

    def eat(self):
        pass

    def sleep(self):
        pass

    def sit(self):
        pass

    def run(self):
        pass

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
dog1.age = 10
dog2.sleep()
