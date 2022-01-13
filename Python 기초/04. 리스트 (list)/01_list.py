# 리스트 : 집합적 자료형, 여러 개의 원소를 가지는 데이터
# 1) 가변적 - 삽입, 삭제, 변경
# 2) 다양한 형식의 데이터 : 숫자, 문자열, 논리
# 3) 리스트 형태 : []

# 리스트 생성
list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

list3 = [1, 2, 3]
print(list3)

list4 = [1, 'apple', 3.5, [10, 20, 30], True]
print(list4)


# 리스트의 요소 출력
for l in list4:
    print(l, end=' : ')
    print(type(l))
print()


# 리스트의 길이 : len(리스트이름)
# 리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 -> 리스트명[index]
print('문자열의 길이 : ', len(list4))
for i in range(0, len(list4)):
    print(list4[i], end=' : ')
    print(type(list4[i]))


# 리스트의 각각의 값은 변수에 저장
nums = [1, 2, 3]
a, b, c = nums
print(a)
print(b)
print(c)


# 리스트 인덱싱(indexing)
# 리스트에서 인덱스 연산자를 통하여 요소를 참조/접근하는 것

a = [1, 'apple', 3.5, [10, 20, 30], True]

print(a[0])  # 첫번째 요소
print(a[-1]) # 마지막번째 요소
print(a[-5]) # 첫번째 요소
print(a[3])
print(a[3][-1])  # 2차원 리스트의 요소 접근 [][]

b = ['apple', 'banana', 'melon']
c = [a, b]
print(c)

# c 리스트 안의 20만 꺼내고 싶으면?
print(c[0][3][1])


# 리스트의 슬라이싱(slicing)
# [start:end] : start에서 end-1 요소까지 선택

# 리스트[:n] => 처음부터 n-1요소까지
# 리스트[start:] => start부터 마지막 요소까지
# 리스트[:] => 모든 요소 (복사)
# 리스트[:-1] => 처음부터 마지막에서 두 번째 요소까지
# 리스트[-1:] => 마지막 요소부터 끝까지
# 리스트[n:] => n부터 마지막 요소까지

a = [1, 'apple', 3.5, [10, 20, 30], True]
print(a[:])
print(a[3:4])
print(a[0:2])


# 리스트 연산
# 1) 리스트 합치기 : +
# 2) 리스트 곱하기 : * (반복)
# 3) 리스트 내용 변경

fruits = ['apple', 'banana', 'melon']
a = [1, 'apple', 3.5, [10, 20, 30], True]

b = fruits + a
print(b)

c = fruits * 3
print(c)

a[3] = 'melon'
print(a)
a[1:3] = [10, 11, 12]
print(a)
a[0] = [-1, -4]
print(a)


# 리스트 복사

# 얕은 복사(shallow copy): 실제 리스트가 복사되지 않고 참조값(주소)만 복사
print('shallow copy -----')
a = [1,2,3,4]
b = a
print(a)
print(b)

a[-1] = 100  # b는 a를 가리키기 때문에 a를 바꾸면 b도 바뀐다
b[1] = 0.5   # b를 바꿔도 a도 바뀐다
print(a)
print(b)

# 깊은 복사(deep copy): 리스트 복사본을 새로 생성하여 반환
# list() 함수 또는 deepcopy() 함수를 사용
print('deep copy -----')
c = list(a)
print(c)
c[0] = 'apple'
print(a)
print(c)

import copy
d = ['a', 'b', 'c']
e = copy.deepcopy(d)

e[0] = 1
print(d)
print(e)

