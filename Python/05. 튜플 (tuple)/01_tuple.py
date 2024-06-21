## 튜플 : tuple()
# 추가, 삭제, 변경 불가

# 튜플 생성 : (), tuple()

t1 = (1, 2, 3)
print(t1)
print(type(t1))

t2 = 4, 5, 6
print(t2)

t3 = tuple([1, 2, 3])
print(t3)

t4 = [1, 2], [3, 4]
print(t4)
print(type(t4[0]))
# 튜플 인덱스로 접근해서 변경 불가
# t4[0] = [-1]

# 튜플의 요소를 변경불가 : 리스트로 변환하여 변경 가능
to_list1 = list(t4)
print(to_list1)
to_list1[1] = 10
t4 = tuple(to_list1)
print(t4)

# 튜플 다루기 : 요소의 위치 index(), 일치 항목의 개수 count()
print(t2.index(5))
print(t2.count(4))

# 튜플 요소 삭제는 불가능
# But 튜플 자체를 삭제하는 것은 가능 : del()
del t1
print(t1)



## 튜플 사용

# 튜플 요소 접근 : indexing
t1 = (10, 30, -10, 50, 100)
print(t1[0] + t1[3])

# 튜플 범위에 접근 : slicing
print(t1[1:3])
print(t1[1:])
print(t1[:])

# 튜플의 덧셈 및 곱셈 연산 : +, *
t2 = ('a', 'b', 'c')
print(t1 + t2)
print(t2 * 3)

# 2차원 튜플
tt = ((1,2,3), (4,5,6), (7,8,9))
print(tt)
print(tt[0][-1])
print(tt[-1])