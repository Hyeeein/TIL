# 특별한 메소드
# __메소드이름__ : 미리 정의되어 있는 메소드

# __ge__() : >= 를 같이 사용할 수 있음
# __gt__() : >
# __lt__() : <
# __le__() : <=
# __ne__() : !=
# __eq__() : ==

# __init__() : 생성자
# __repr__() : 인스턴스 print() 문으로 출력
# __add__() : +
# __del__() : 소멸자, 인스턴스를 삭제

# 선 (line) 클래스
# 필드 : 길이, 색상, 두께
# 메소드 : 더하기, 크기 비교

class Line:
    def __init__(self, length = 0):
        self.length = length
        print(f'{self.length}의 길이 선분이 생성되었습니다.')

    def __add__(self, other):   # 인수 other가 자동으로 들어옴
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __mul__(self, other):
        return self.length * other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self, other):
        return self.length != other.length

    def __del__(self):
        print(self.length, '길이의 선분이 삭제되었습니다.')

    def __repr__(self):
        return f'선의 길이: {self.length}'    # 문자열 return

line1 = Line(10)
line2 = Line(5)
print('line1:', line1.length)
print('line2:', line2.length)
print('line1 + line2 =', line1 + line2)
print('line1 > line2 =', line1 > line2)
print('line1 == line2 =', line1 == line2)
print(line1)
print(line2)