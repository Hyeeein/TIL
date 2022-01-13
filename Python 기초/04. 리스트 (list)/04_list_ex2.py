## 연습문제 1: 학생 10명의 점수를 입력 받아서 리스트로 생성하고 총점과 평균을 계산하여 출력
# 80점 이상의 학생의 수도 출력하기 (list_ex에서 살짝 변경)

scores = []
sum = 0
num = 0

for i in range(1, 11):
    score = int(input('학생%d 점수 입력 : ' %i))
    sum += score
    scores.append(score)
    if score >= 80:
        num += 1
avg = sum/10

print(scores)
print('총점 : %d' % sum)
print('평균 : %.2f' % avg)
print('80점 이상의 학생 : %d' % num)


## 1번 예시 답안
#
# scores = []
# n = int(input('학생 수 입력 : '))  # 학생 수를 n으로 입력받고 싶으면 이렇게 수정해서 활용할 수도 있음
# total = 0
# cnt = 0
#
# for i in range(1, n+1):
#     score = int(input('학생' + str(i) + ' 점수 입력 : '))
#     scores.append(score)
#
# print(scores)
# for score in scores:
#     if score >= 80:
#         cnt += 1
#     total += score
#
# print('총합은 %d이고, 평균은 %.2f' %(total, total/len(scores)))
# print('80점 이상 학생 %d명' % cnt)


## 연습문제 2 : 엔터키를 입력 받을 때까지의 점수들을 계산

scores = []
total = 0
cnt = 0
i = 1

while True:
    score = int(input('학생' + str(i) + ' 점수 입력 : '))
    if score -- '':
        break
    scores.append(score)
    i += 1

print(scores)
for score in scores:
    if score >= 80:
        cnt += 1
    total += score

print('총합은 %d이고, 평균은 %.2f' %(total, total/len(scores)))
print('80점 이상 학생 %d명' % cnt)