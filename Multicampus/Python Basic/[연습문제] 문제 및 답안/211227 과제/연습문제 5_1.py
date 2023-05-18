## 연습문제 5-1
# 만든 날짜 : 2021-12-27
# 만든이 : 박혜인

students = [
    {'name': '홍길동', 'korean': 87, 'math': 98, 'english': 88, 'science': 95},
    {'name': '이몽룡', 'korean': 92, 'math': 98, 'english': 96, 'science': 98},
    {'name': '성춘향', 'korean': 76, 'math': 96, 'english': 94, 'science': 90},
    {'name': '변학도', 'korean': 98, 'math': 92, 'english': 96, 'science': 92},
    {'name': '박지성', 'korean': 95, 'math': 98, 'english': 98, 'science': 98},
    {'name': '류현진', 'korean': 64, 'math': 88, 'english': 92, 'science': 92}
]

print('이름 \t 총점 \t 평균')

for name in students:
    sum = 0 ; avg = 0

    for score in name.values():
        if type(score) == str:
            name2 = score
        elif type(score) == int:
            sum += score
    avg = sum/4
    print('{} \t {} \t {}'.format(name2, sum, avg))


## 예시 답안 (students는 동일)
#
# print('이름 \t 총점 \t 평균')
#
# for std in students:
#     total = std['korean'] + std['math'] + std['english'] + std['science']
#     avg = total / 4
#     name = std['name']
#     print(f'{name}\t{total}\t{avg}')

