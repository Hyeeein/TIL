# % 서식문자열: %s, %d, %f, %c

# format() 함수 사용
print(format(1.234567, '10.3f'))

# string.format()
# 1) '문자열 {위치인덱스}'. format(변수)
print('Name:{0}, Phone:{1}' .format('hipark', 1234-123))
s2 = '{0:d} {1:5d} {2:05d}' .format(123,123,123)
name = 'hipark' ; phone = '123-1234'
print('이름은 {}이고, 폰 번호는 {}' .format(name, phone))

# 2) '문자열 {변수}' .format(변수 = 값)
print(f'이름은 {name}이고, 폰 번호는 {phone}' .format(name="이몽룡", phone='123-111'))

# 3) '문자열 {위치인덱스: 포맷코드}'.format(변수)
s3 = '{0:.2f} {1:10.2f}' .format(3.14, 3.14)


# f'String 사용
# 파이썬 3.6 이상

print(f'이름은 {name}이고, 폰번호는 {phone}')
print(s1)
print(s2)
# print('{2:d} {1:d} {0:d}'.format(100, 200, 300))

tea = 'coffee'
n = 5
s3 = f'나는 {tea}를 좋아해요. 하루에 {n}잔 마셔요'
print(s3)

for month in ['1월', '2월', '3월']:
    print(f'이번 달은 {month} 입니다')