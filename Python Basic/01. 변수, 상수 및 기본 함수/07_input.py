# 입력 함수 : input('프롬프트 문자열')
# 키보드로부터 값을 입력 받아서 처리하기 위해 사용
# 입력함수를 수행한 결과, 반환된 데이터 유형은 문자열

# x = 100
# y = 300
# print(x + y)
#
# name = input('이름: ')    # type은 문자열
# age = input('나이: ')     # 그래서 나이 str을 int로 변환해주어야 함
# print('이름은 %s이고, 나이는 %d입니다' % (name, int(age))


## 연습문제 1 : 두 정수를 입력받아 사칙연산 결과 출력하기

a = int(input("숫자 1: "))
b = int(input("숫자 2: "))

print("합:", a+b)
print("차:", a-b)
print("곱:", a*b)
print("나누기:", a/b)

# 포맷 형태로 만들고 싶다면
sum = a + b
print("합: %d" % sum)
sub = a - b
print("차: %d" % sub)
mul = a * b
print("곱: %d" % mul)
div = a / b
print("나누기: %.2f" % div)

'''
# 이렇게도 쓸 수 있음
num1 = int(input('숫자1 : '))
num2 = int(input('숫자2 : '))
result = num1 + num2
print('합 : %d' % result)
result = num1 - num2
print('차 : ', result)
result = num1 * num2
print('곱 : ', result)
result = num1 / num2
print('나누기 : ', result)
'''

'''
합 = int(num1)+int(num2)
차 = int(num1)-int(num2)
곱 = int(num1)*int(num2)
나누기 = int(num1)/int(num2)

print(합, 차, 곱, 나누기)
'''


## 연습문제 2
# 출력결과
# 국어점수 입력 : 90
# 영어점수 입력 : 90
# 수학점수 입력 : 70
# 총점 : 250
# 평균 : 83.33

kor = int(input("국어점수 입력: "))
eng = int(input("영어점수 입력: "))
math = int(input("수학점수 입력: "))

sum = kor + eng + math
avg = sum / 3

print("총점: %d" % sum)
print("평균: %.2f" %avg)


## 연습문제 3 : BMI 지수 계산 (몸무게 / (키*키)), 몸무게는 kg, 키는 m 단위

weight = float(input("몸무게(kg): "))
height = float(input("키(미터): "))

bmi = weight / (height * height)
print("당신의 BMI는 %.2f입니다." % bmi)
# print("당신의 BMI는 {:.2f} 입니다." .format(bmi))
