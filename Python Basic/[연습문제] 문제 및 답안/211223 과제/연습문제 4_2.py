# 연습문제 4-2 (12월 23일 과제)
# 만든 날짜: 2021-12-26
# 만든이: 박혜인

str_data = "{a1:20},{a2:30},{a3:15}, \
            {a4:50},{a5:-14},{a6:15},\
            {a7:20},{a8:70},{a9:-100}"

temp1 = str_data.split(':')
data_split = []

for i in temp1:
    if '}' in i:
        temp2 = []
        temp2 = i.split('}')

        for j in temp2:
            if '{' not in j and j != '':
                data_split.append(int(j))

sum = 0

for k in data_split:
    sum += k

print('총 합은', sum)


## 예시 답안 1
# str_data = "{a1:20},{a2:30},{a3:15}, \
#             {a4:50},{a5:-14},{a6:15},\
#             {a7:20},{a8:70},{a9:-100}"
#
# split_data = str_data.split(',')
# total = 0
# n = 0
# for data in split_data:
#     item = data.split(':')
#     item2 = item[1].split('}')
#     score = int(item2[0])
#     print(score)
#     total += score
#     n += 1
#
# print('총점: %d, 평균: %f' %(total, total/n))
