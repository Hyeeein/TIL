## 튜플에 데이터를 추가할 수 있는 방법

# 1) 리스트로 변경한 후 값을 추가하고 다시 튜플로 변경 (정석)
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)

# 2) + 연산 수행 (야매)
myTuple = (10, 20, 30)
update = (40,)   # 콤마(,)가 없으면 정수로 인식. 있어야만 튜플로 인식
result = myTuple + update
print(result)