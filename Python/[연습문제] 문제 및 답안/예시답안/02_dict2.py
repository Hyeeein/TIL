# # 문제. 음식 정보를 딕셔너리로 생성, 음식정보들은 리스트로 구성
#
# data1 = {'name':'버섯불고기',
#          'class':'한식',
#          'type':'불고기',
#          'ingr':['소고기','양파','간장', '설탕'] }
#
# data2 = {'name':'카레덮밥',
#          'class':'양식',
#          'type':'덮밥',
#          'ingr':['카레','감자','양파', '당근'] }
#
# datum = [data1, data2]
#
# # 음식정보 출력하기
# i=1
# for data in datum:
#     print('음식'+str(i))
#     for d in data.keys():
#         print(d ,':', data.get(d) )
#     i +=1
#     print('--------------')

def sum_data(list_data_a, list_data_b):
    for i in list_data_a:
        for j in list_data_b:
            result = i + j
    return result

a = [1, 2]
b = [3, 4]
print(sum_data(a, b))