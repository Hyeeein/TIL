# 파일 내에서 검색
# seek (offset, whence) :
#       - offset : 상대위치, 시작 위치로부터 열의 위치
#       - whence : 위치
#                  0 : 파일 시작 위치 / 1 : 현재 위치 / 2 : 파일의 끝
# seek(0, 0) : 시작 위치로부터 0열의 위치 => 0행 0열
# seek(10, 0) : 시작 위치로부터 오른쪽으로 10열의 이동한 위치 => 0행 10열
# seek(0, 2) : 파일의 끝으로부터 0열의 위치 => 0행 0열

f = open('test2.txt', 'r')
# f.seek(0, 0)    # 0행 0열
# f.seek(3, 0)
f.seek(-2, 2)      # 파일의 마지막에서 2열 이동한 위치
lines = f.readlines()
print(lines)
f.close()

# \r : carriage return
# \n : line feed

# 01234\r\n
# abced\r\n
# 가나다라마     : 2씩 증가함