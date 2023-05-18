# 내부 함수 : 함수 안에 있는 함수
# 함수가 정의된 그 범위에서만 사용

def outFunc(x, y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc(10,20))
