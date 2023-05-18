# 함수: 함수이름()
#      함수이름()으로만 호출
#      input(), print(), len(), del() : 내장함수
#      사용자 정의 함수

# 메소드: 메소드이름()
# 클래스의 멤버인 객체를 통해서 사용
# string 객체이름.find()

# 리스트에서 사용되는 함수 : len() => 리스트의 길이 반환(원소의 개수)
a = [1,2,3,4,5]
print(len(a))

# .count() 메소드 : 리스트 내의 특정한 요소의 개수를 세기
b = [1,2,3,4,2,3,1,0]
print(b.count(3))

# 리스트의 요소를 추가 : append(), insert()
# append() : 리스트의 끝에 추가
a.append(1)
print(a)
a.append([9, 10])
print(a)

# insert(위치, 값) : 특정 위치에 값을 삽입
a.insert(1, 200)
print(a)

values = [] # 빈 리스트 생성
values.append(10)
values.append(20)
values.append(3)
print(values)

## 예: 10명의 학생의 점수를 입력받아서 리스트를 생성하고 출력
scores = []
for i in range(10):
    scores.append(int(input('점수입력: ')))
print(scores)
