# readline() : 한줄씩 읽어오기

# 한줄만 읽어오기
f = open('test.txt', 'r')
line = f.readline()     # 첫 번째 라인 1개 읽기
print(line)
f.close()

# 한줄씩 읽어오기
f2 = open('test.txt', 'r')

while True:
    line = f2.readline()    # 이미 뒤에 \n이 붙어있음
    if not line:
        break
    print(line)             # 얘도 이미 \N이 붙어있으므로, 두 줄이 띄워져서 나옴
    # print(line, end = '')

f2.close()

# readlines() : 전체 라인을 읽어오기
# 리스트로 반환함

f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end = '')
f.close()

f = open('test.txt', 'r')
for line in f:
    print(lines)
f.close()