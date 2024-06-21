# 클래스메서드
# : 인스턴스를 통하지 않고, 메서드를 클래스에서 바로 호출
# : 메서드 내에서 클래스 변수, 클래스 메서드를 접근할 때 사용함

# @classmethod를 메서드 위에 붙임
# : 메서드 내에 인수로 cls를 지정 (cls : class의 약어)

'''
# 형식

class 클래스이름:
    @classmethod
    def 메서드명(cls, 매개변수들):
        문장들

# 호출형식
클래스이름.메서드명(인수들)
'''

# 클래스 변수 이용
class Person:
    count = 0       # 클래스변수
    def __init__(self, name):
        self.name = name
        Person.count += 1

    def printCount(self):
        print(f'{self.count}명이 태어났습니다')

man1 = Person('Kim')
man2 = Person('Lee')
man1.printCount()
man2.printCount()     # 지금은 공유되어 있는 것

#
class Person:
    count = 0       # 클래스변수
    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def printCount(cls):    # 클래스메소드를 사용하면 self를 사용하지 않고 cls를 사용
        print(f'{cls.count}명이 태어났습니다')

man1 = Person('Kim')
man2 = Person('Lee')
Person.printCount()     #