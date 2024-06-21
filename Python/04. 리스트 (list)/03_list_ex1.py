## 연습문제 1 : 학생 10명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하고 출력

scores = []
sum = 0

for i in range(1, 11):
    score = int(input('학생%d 점수 입력 : ' %i))
    sum += score
    scores.append(score)
avg = sum/10

print(scores)
print('총점 : %d' % sum)
print('평균 : %.2f' % avg)