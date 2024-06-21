# 다중상속 : 다이아몬드 상속의 예
# 동일한 이름의 메소드를 갖는 경우
# 메소드 탐색 순서(Method Resolution Order:MRO) 규칙에 따라 처리

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B:
    def greeting(self):
        print('안녕하세요. B입니다.')

class C:
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

X = D()
X.greeting()    # 안녕하세요. B입니다.

# 클래스.mro()를 이용하여 메서드 호출 순서 확인
print(D.mro())