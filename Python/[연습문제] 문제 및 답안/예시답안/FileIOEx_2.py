# 2. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
#  한줄의 두 숫자를 더한 연산 결과를 파일로 저장하기

# list_num.txt 파일을 읽기

# with open('list_num.txt','r') as f:
#     data = f.readlines()
#
# with open('output.txt','w') as f:
#     for d in data:
#         if  d != '\n':
#             value =d.replace('\n','').split()
#             print(value)
#             result = int(value[0])+int(value[1])
#             f.write(f'{value[0]}+{value[1]}={result}\n')
#         else:
#             continue
#
# with open('output.txt','r') as f:
#     output = f.read()
#
# print(output)


# 파일을 읽어오고 파일에 쓰고, 숫자에 대해 연산하는 기능은 함수로 정의해서 사용
# sum(inputfile객체, 저장파일명)

def sum(input_file, ouput_filename) :
    list_file = input_file.readlines() #전달된 파일객체에서 데이터 읽어오기
    output_file = open(ouput_filename,"w")
    #리스트 각 요소에 대하여 필요없는 문자 제거 작업
    for i in range(0,len(list_file)) :
        list_file[i]=list_file[i].replace("\n","")
        if list_file[i] !='' :
            value1,value2 = list_file[i].split()
            sum = int(value1) + int(value2)
            new_line = value1+'+'+value2+'='+str(sum) +'\n'
            output_file.write(new_line)
        else :
            continue
    output_file.close() #파일 닫기

main : 프로그램 실행코드
if __name__ =='__main__':
    input_file = open("../../../Users/phi49/Downloads/Day9/list_num.txt", "r")
    sum(input_file, "output.txt") # 입력 파일 객체를 인수로 전달
    input_file.close()

# 홍지수 작성
# def sum(input_file,filename):
#     with open(input_file,'r') as f:
#         lines = f.readlines()
#         lst=[]
#         for line in lines:
#             if line != '\n':
#                 word_num1, word_num2 = line.split()
#                 num1 = int(word_num1)
#                 num2 = int(word_num2)
#                 addUp = float(num1 + num2)
#                 cal = '%d+%d=%.1f' %(num1, num2, addUp)
#                 lst.append(cal)
#
#     with open (filename,'w') as f:
#         for i in lst:
#             f.write(i + '\n')
#
# if __name__ == '__main__':
#     sum('list_num.txt','new_cal.txt')

# 이유진 작성
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

# 강중모 작성
# def sum(inputname, savename):
#     with open('num.txt', 'r') as f:
#         tmp = f.read().replace('\n', ' ')
#     lst = tmp.split()
#     a, b = lst[0::2], lst[1::2]
#     lst2 = [[a[i], b[i]] for i in range(len(a))]
#
#     with open(savename, 'w') as f:
#         for ls in lst2:
#             val1 = int(ls[0])
#             val2 = int(ls[1])
#             f.write(f'{val1}+{val2}={float(val1 + val2)}\n')
#
# if __name__ == '__main__':
#     sum('num.txt', 'calc.txt')