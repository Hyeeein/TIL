# 위치 인수와 키워드 인수

def sumN(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    return a+b+c

# 위치에 의해 인수를 구별하는 방식 : 기본
print(sumN(10, 20, 30))

# 키워드 인수 전달
#print(sumN(a=10, c=30, b=20))
print(sumN(c=10, a=50, b=-10))
# print(sumN(c=10, 50, -10))  # 오류 : 키워드 인수 뒤에 위치 인수를 올 수 없다