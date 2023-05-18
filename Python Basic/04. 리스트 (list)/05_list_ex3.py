## 연습문제 1

# 각 학생별 점수 리스트 생성
kim = [90, 85, 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 70]

students = [kim, choi, kang, lee]

# 학생별 총점과 평균점수 출력
for i in range(4):
    sum = 0 ; avg = 0
    for j in range(3):
        sum += students[i][j]
    avg = sum/3
    print('%s의 총점은 %d이고, 평균은 %.2f입니다' %(students[i], sum, avg))

# # 예시답안
# std_id = 1
# for std in students:
#     total, avg = 0, 0
#     total = sum(id)
#     print('학생 %s의 총점은 %d 평균은 %.2f %(str(i), total, total/n')


# 과목별 총점과 평균점수 출력
for i in range(3):
    sum = 0   ;  avg = 0
    for j in range(4):
        sum+= students[j][i]
    avg = sum/4
    print('%d번째 과목의 합은 %d이고, 평균은 %.2f입니다' %(i+1, sum, avg))

# # 예시답안
# std_n = len(students)
# n = len(students[0])
# for i in range(n):
#     total = 0
#     for id in range(std_n):
#         total += students[id][i]
#     print('과목 {}의 총점은 {} 평균은 {}' .format(str(i), total, round(total/std_n, 1))
