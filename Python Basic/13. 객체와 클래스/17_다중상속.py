'''
다중상속 : 여러 클래스에서 상속을 받음

형식
class 클래스 이름 (부모클래스1, 부모클래스2, ...):
    pass
'''

# 예시
class Person(object): # 여기서 object는 쓰나 안 쓰나 같음
    def __init__(self, name='', age = 0):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

class university():
    def __init__(self, departmemt='', grade=''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print('학점관리')

class Undergraduate(Person, university):
    def study(self):
        print('공부하기')

kim = Undergraduate()
kim.name = 'Kim'
kim.age = 20

kim.greeting()
kim.manageScore()
kim.study()

