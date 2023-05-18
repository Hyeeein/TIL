# 정적메서드 (static method)
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# 메서드 위에 @staticmethod 를 붙이고, self를 넣지 않는다
# -> 결국 인스턴스 변수와 인스턴스 메서드가 필요하지 않고, 순수함수로 만들어서 사용함

class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

# calc1 = Calc()
# calc2 = Calc()
# print(calc1.add(3, 2))  # 필드를 쓰지 않음.
# print(calc2.add(3, 2))

# 위처럼 인스턴스를 생성하여 메서드를 호출하지 않고
# 클래스 이름으로 메서드를 호출함
# 정적 메서드 호출방식 : 클래스이름.정적메서드(*args)
print(Calc.mul(10, 30))
