# Set : 집합 형태의 자료 구조 (집합 자료형)

# set 생성
s1 = {1,2,3,4,5}
s2 = set([3,4,7,8,9])
s3 = set()

print(s1)
print(s2)
print(s3)
print(type(s1))
# print(dir(s1))
print(type(s3))

# ['__and__', '__class__', '__class_getitem__', '__contains__',
#  '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__',
#  '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__',
#  '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
#  '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
#  '__str__', '__sub__', '__subclasshook__', '__xor__',
#  'add', 'clear', 'copy', 'difference', 'difference_update',
#  'discard', 'intersection', 'intersection_update', 'isdisjoint',
#  'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
#  'symmetric_difference_update', 'union', 'update']


# set의 특징
# 1) 중복을 허용하지 않음 : unhashable type
# 2) 입력순서와 출력되는 순서가 다를 수 있음

s4 = {1,3,2,2,5,4,3}
print(s4)

# 3) 인덱스 사용 불가 : 이미 포함되어 있는 요소를 변경할 수 없음

# print(s4[0])

# 4)추가 가능 : add(), update()

# 1개 추가 : add()
s4.add(10)
print(s4)

# 여러 개 추가 :update()
s4.update([5,6])
print(s4)

# 5) 집합 안에 변경가능한 항목 포함 불가능
#    : 리스트 포함 불가, 튜플 포함 가능

#s5 = {1, 2, [3, 4]}
s6 = {1 ,2 , (3,4)}
print(s6)

# 6) 요소 삭제 가능

# s6.remove(1)
# print(s6)

# s6.discard(1)
# print(s6)

# s6.remove(10)  # 요소 값이 없는 경우 에러
s6.discard(10)  # 요소 값이 없는 경우 에러 없음

# 요소 전체를 지움 => 빈 집합
s6.clear()
print(s6)

del s6
# print(s6)
