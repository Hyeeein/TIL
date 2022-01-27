# 파이썬이 처리하는 자료형(data type)
# 정수(int), 실수(float), 문자열(str), 부울(bool)

# 정수 : 2진수, 10진수, 8진수, 16진수
# 실수 : 3.14, 1.2e3
# 문자열 : '', ""
# 부울(논리값) : True, False

a = 100
b = 3.14
c = 'name'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형변환 : int(), float(), str()

# str() : 문자열로 변환
print(type(str(100)))

str1 = str(3.14)
print(str1 + 'pie')

str2 = '123'

# int(문자열) : 문자열을 정수형으로 변환
num1 = int(str2)
print(type(num1))
print(num1+10)

# float(문자열) : 실수로 변환
num2 = float(str1)
print(type(num2))
print(num2+10)


# int(문자열, 진수) : 해당 문자열의 진법을 나타내줌
print(int('1010', 2))  # 출력 결과는 2진수를 10진수 형태로 바꿔서 출력
print(int('1010', 8))  # 출력 결과는 8진수를 10진수 형태로 바꿔서 출력
print(int('1010', 10))
print(int('1010', 16))
