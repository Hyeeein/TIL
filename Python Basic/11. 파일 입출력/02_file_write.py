# 텍스트 파일에 쓰기 : write()

# data = 'Hi'
# f = open('file2.txt', 'w')
# f.write(data)       # 파일에 데이터 쓰기
# f.close()
#
# data = '안녕하세요'
# f = open('file2.txt', 'w')  # 한글이 ANSI 저장
# f.write(data)   # 파일에 data 쓰기
# f.close()
#
# data = '안녕하세요'
# f = open('file3.txt', 'w')
# f.write(data)
# f.close()


### 연습문제 1 : 파일에 쓰기
f = open('file4.txt', 'w', encoding='utf-8')

for i in range(1, 11):
    data = '%d행\n'%i
    f.write(data)