# 문제 2 : 한 줄의 두 숫자를 더한 후 연산 결과를 파일로 내보내는 프로그램
# 만든 날짜 : 2022-01-03
# 만든이 : 박혜인

def sum(f1, f2):
    f1 = open('list_num.txt', 'r')
    f2 = open('list_calc.txt', 'w')

    list_num = f1.readlines()
    f1.close()

    for num in list_num:
        # 해당 행이 공백이 아닌 경우 (숫자가 있는 경우)
        if num.isspace() == False:
            num_split = num.split(' ')
            result = int(num_split[0]) + int(num_split[1])
            f2.write(f'{int(num_split[0])} + {int(num_split[1])} = {result}\n')
        else:
            continue

sum('list_num.txt', 'list_calc.txt')


### ---------------------- ###
### 다른 분 답안 ###
#
# def sum(load_path,save_path):
#     with open(load_path, 'r') as f:
#         lines = f.readlines()
#         with open(save_path, 'w') as w:
#             for line in lines:
#                 a, b = map(int, line.split())
#                 w.write(f'{a}+{b}={a+b}\n\n')
#
#
# if __name__ == '__main__':
#     path = '/Users/iyujin/develop/pythonProject/Day8_0103/FileIO'
#     load_path = path + '/list_num.txt'
#     save_path = path + '/list_calc.txt'
#     sum(load_path,save_path)
