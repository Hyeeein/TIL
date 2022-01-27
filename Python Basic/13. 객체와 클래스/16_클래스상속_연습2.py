# 사람 클래스와 이를 상속받은 학생 클래스 정의
# Person : 변수 name, age / 메소드 greeting
# Student : 변수 department, grade / 메소드 study

class Person():
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('안녕하세요')

class Student(Person):
    department = ''
    grade = ''

    def __init__(self, name, age, departmemt, grade):
        super().__init__(name, age)
        self.department = departmemt
        self.grade = grade

    def study(self):
        print('공부하자')

p1 = Person('멀티', 20)
p1.greeting()
s1 = Student('경제학과', 'A')
s1.study()