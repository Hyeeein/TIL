# literal : 정수, 실수, 문자, 문자열, 논리, 특수(None)

'''
여러 줄 주석
'''

# 정수 리터럴
a = 10      # 10진수
b = 0b1111  # 2진수
c = 0o61    # 8진수 (2진수로 포현하면 0b110001, 뒤부터 3자리씩 끊어서 값을 냄)
d = 0x1f2c  # 16진수 (2진수로 표현하면 0b0001111100101100, 뒤부터 4자리씩 끊어서 값을 냄)

print(a, b, c, d)

# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234e5

print(f1, f2, f3)

# 문자 리터럴
c1 = 'a'
c2 = 'B'

print(c1, c2)

# 문자열 리터럴
str1 = '박혜인'
str2 = "Hello"
str3 = """안녕하세요 Hello
반갑습니다 Nice to meet you"""       # 여러 줄로 표현할 때
str4 = '''안녕하세요 Hello
반갑습니다 Nice to meet you'''       # 여러 줄로 표현할 때

print(str1, str2)
print(str3)
print(str4)

# 논리값 리터럴 : True False
t = True
f = False
print(t, f)

# 특수 리터럴 : None
name = '박혜인'
phone = ''
address = None      # type 출력하면 NoneType

print(name, phone, address)
print(type(address))
print(type(phone))
