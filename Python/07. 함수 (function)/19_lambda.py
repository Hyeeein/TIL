# lambda(람다)함수 : 함수를 한줄로 간단하게 작성

# 일반적인 함수: 함수의 이름과 매개변수가 있음
def add(x, y):
    result = x + y
    return result
print(add(10, 20))

# 람다 함수
add2 = lambda x, y : x + y
print(add2(10, 20))

# 매개변수에 기본값을 설정
add3 = lambda x = 10, y = 10 : x + y
print(add3(10, 20))
print(add3())

# 문제 : 리스트의 각 요소에 10을 더하는 함수
# def add10(num):
#     for i in range(len(num)):
#         num[i] += 10

num = [1, 3, 4, 10]
# add10(num)
# print(num)

# 10을 더하는 함수
def add10(num):
    return num + 10

print(num)

for i in range(len(num)):
    num[i] = add10(num[i])

print(num)

# map() 함수
num2 = list(map(add10, num))
print(num2)

# lambda() & map() ==> 모르겠음. 다시 공부하기
num3 = list(map(lambda num: num+10, num))
print(num2)


# map() 함수 : 리스트나 튜플, 문자열 등 반복가능한 구조의 요소별로 지정된 함수를 적용하여
#             원본은 변경하지 않고 list, tuple 형태로 반환
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

# 문제. 실수형 요소를 갖는 리스트를 정수형 요소가 든 리스트로 변환

number1 = [3.5, 3.4, 2.0, 4.6]

# map을 이용하는 경우
new_number = list(map(lambda num: int(num), number1))
print(new_number)
# print(list(map(int, number1)))으로 하면 더 간단함

# for을 이용하는 경우 (원본 리스트 수정)
for i in range(len(number1)):
    number1[i] = int(number1[i])
print(number1)


# (lambda 매개변수들: 식) (인수들)
# 람다 표현식을 변수에 할당하지 않고, 그 자체를 호출해서 사용
(lambda x: x+10)(25)

# 람다 표현식 안에서 변수 생성 불가
# (lambda x, y: y=10; x+y)(5)
y = 10
(lambda x : x + y)(5)    # 이런 경우는 가능


# 문제 2. 두 리스트의 각 자리수의 값을 합해서 새로운 리스트를 생성 (다시 해보기)
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# def 함수를 사용해서 리스트 생성
def addList(x, y):
    new_list = []
    for i in range(len(x)):
        new_list.append(x[i] + y[i])
    return new_list

print(addList(list1, list2))

# lambda & map 사용해서 생성
new_list = list(map(lambda x, y: x + y, list1, list2))
print(new_list)
