# 앞에서 작성한 Dog 클래스에서
# 1. 객체 간의 크기를 비교하는 메소드 작성
# 2. 객체 간의 나이를 더하고, 빼고, 곱하고, 나누는 메소드 작성
# 솔직히 모르겠다 ...

class Dog():
    def __init__(self, breed = 'Maltese', size = 2, age = 0, color = 'white'):
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

    def __repr__(self):
        info = f'품종 : {self.__breed} \n크기 : {self.size} \n나이: {self.age} \n색상: {self.color}'
        return info

    # 여기부터 추가한 코드 #
    # 크기 비교
    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    # 나이 사칙연산
    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __divmod__(self, other):    # 몫과 나머지 모두 리턴
        if other.age != 0:
            return self.age / other.age
        else:
            print('0으로 나눌 수 없습니다.')

dog1 = Dog()
dog2 = Dog()
if dog1 > dog2:
    print('dog1이 dog2보다 크네요!')
elif dog1 == dog2:
    print('dog1과 dog2는 비슷해요!')
else:
    print('dog2이 dog1보다 크네요!')