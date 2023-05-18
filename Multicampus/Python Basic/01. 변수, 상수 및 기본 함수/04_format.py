# format() 함수
# format(실수, '전체 자리수, 소수 이하 자릿수 <서식기호>')

cTemp = 30
print(format(cTemp, '.2f'))

## 연습문제 1 : 총점과 평균을 구해서 출력하기
# 출력 결과는 '총점: 250, 평균: 83.33' 형태로 나오게

kor = 90
eng = 80
math = 80

sum = kor + eng + math
avg = sum / 3

print('총점: %d, 평균: %.2f' % (sum, avg))
print(format('총점: %d, 평균: %.2f' % (sum, avg)))  # format 함수를 쓸 경우

# ----------

# .format() 함수와 {}을 사용하여 서식 지정

print(format(1234.567, '10.2f'))
print('{:.2f}' .format(1234.567))
print('name: {}, phone: {}' .format('박혜인', '010-1234-1234'))
print('name: {1}, phone: {0}' .format('010-1234-1234', '박혜인'))

print('{0:d}, {1:d}' .format(100, 123))  # 0과 1 뒤에 있는 d는 %d와 같은 것
print('{1:d}, {0:d}' .format(100, 123))
print('{0:d}, {1:5d' .format(100, 123))
print('%d %5d %10d' %(123, 123, 123))