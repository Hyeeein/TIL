# 2021-12-20 (월)

# 변수의 특징
# 1) 레퍼런스 : 값(객체)이 저장된 메모리의 위치를 가리키는 레퍼런스(reference : 참조)
# 2) 동적 타이핑: 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
#    type 검사 (자료형이 지정되어 있지 않다)
# 3) 변수는 이름을 가지고 있다
# 4) 변수는 다른 값을 저장할 수 있다 (값 변경 가능)
# 5) 변수는 선언이 필요없다
# 6) 변수는 객체가 저장된 주소값이 저장된다

# 자바는 int x 처럼 아예 형을 고정하는데 파이썬은 12번째 줄처럼 데이터 형에 상관없이 사용가능
# 자바에서는 int x
#          x = 100.0 (오류)

x = 10
print(x)
id(x)         # 파일 실행에서는 뜨지 않음 Console 화면에서만 id가 뜸
              # id는 변수가 가리키는 값(객체)의 주소
type(x)       # 변수가 가리키는 값의 형식

y = 'hello'   # 데이터 형이 상관없이 출력가능 => 동적 타이핑이라고 함
print(y)
y = 'haha'
print(y)
y = 100
print(y)
y = 10.5

y = [10, 30, 40]  # 리스트형 데이터
id(y)
type(y)

z = y  # y가 가리키는 값을 z가 가리키게 됨
       # y값을 z가 참조했기 때문에 id값을 콘솔창에서 구해보면 같은 값이 나옴

# 변수 이름
# 1) 대소문자 구분 : C언어 기반 -> 대문자 X와 소문자 x를 다 구분한다
# 2) 영문자, 숫자, 밑줄(_)
# 3) 중간에 공백은 쓸 수 없음 / 여러 개의 단어로 표현할 수도 있음
#    snake : std_name
#    comel : stdName
# 4) 예약어는 변수명으로 사용할 수 없다 (입력했을 때 파란색 글자색으로 나오는 것)

# 식별자 : 변수, 상수, 함수, 사용자 정의 타입
# id(), type()

import keyword
keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

len(keyword.kwlist)
# 35

# 변수에 값 저장 : 할당(assign)
# 1) 변수이름 = 값
a = 100

# 2) 변수1, 변수2, 변수3 = 값1, 값2, 값3 (다른 언어에서는 이렇게 할 수 없음)
a, b, c = 1, 2, 3

# 3) 변수 1 = 변수 2 = 변수 3 = 값 1
a = b = c = 100

# 4) 변수값 교환 (swap) : 변수 1, 변수 2 = 변수 2, 변수 1
a, b = b, a

# 변수 삭제: del 변수명
del z


# 문자열: '', "", ''' ''', """ """
# 문자열 + 문자열 = 하나의 문자열로 합쳐줌

# print 문
# 1) print(값)
# 2) print(변수명)
# 3) print(값, 변수명, ...)

## 문제 1 : 자신의 이름과 나이를 변수에 저장한 후, print()를 이용하여 한 줄로 출력하시오.
## 이름은 문자열로, 나이는 숫자로 저장

name = "박혜인"
age = 22
print("이름은 " + name + "이고, 나이는 " + str(age) + "살 입니다.")


# 포맷 코드 사용

# 형식: print('서식' % 값)
# 형식: print('문자열 %d 문자열' % 변수)
# 서식: %d %f %s %o %x %%

name = "박혜인"
age = 22
print('나이 : %d살' % age)
print('이름 : %s' % name)

print('나이 : %d살\n이름 : %s' %(age, name))  # 묶어서 쓰려면 이렇게 써도 됨


## 문제 2 : 변수 선언 후 값 저장하여 출력 / 변수 : name, no, year, grade, average

name = "홍길동"
no = 2016001
year = 4
grade = "A"
average = 93.5

print("성명 :", name)
print("학번 :", no)
print("학년 :", year)
print("학점 :", grade)
print("평균 :", average)

# %n.mf : 전체 n자리, 소수점 이하 자리수 m
# 예: 10.3f : 전체 10자리, 소수점 이하 자리수 3 => ______.___