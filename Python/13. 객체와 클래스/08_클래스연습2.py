# 앞에서 작성한 Dog 클래스에서
# 1. 디폴트 매개변수를 갖는 생성자를 정의
# 2. 필드 중 breed는 비공개 필드로 정의
# 3. 필드의 값을 가져오고, 변경하는 메소드를 정의
# 4. sleep(), sit(), run(), eat() 메소드의 내용을 정의
#    잠자기  , 앉다  , 뛰다  , 먹다 등의 내용이 출력되도록 정의

# 5. 인스턴스를 생성하되, 인수의 수를 다양하게 입력하여 생성하는 코드 작성
# 6. 인스턴스를 이용하여 개의 정보를 출력
#    - 품종, 나이, 색상, 크기 등의 정보를 출력

class Dog():
    def __init__(self, breed = 'Maltese', size = 'Medium', age = 0, color = 'white'):
        self.__breed = breed
        self.size = size
        self.age = age
        self.color = color

    def getBreed(self):
        return self.__breed

    def setBreed(self, breed):
        self.__breed = breed

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def Eat(self):
        print('먹기')

    def Sleep(self):
        print('잠자기')

    def Sit(self):
        print('앉기')

    def Run(self):
        print('뛰기')

    def printInfo(self):
        info = f'품종 : {self.__breed} \n크기 : {self.size} \n나이: {self.age} \n색상: {self.color}'
        print(info)

dog1 = Dog()
dog2 = Dog('말티즈', 'small')
dog3 = Dog('추추', 'medium', 1)

print(dog1.getBreed())
dog1.setBreed('말티즈')
print(dog1.getBreed())
