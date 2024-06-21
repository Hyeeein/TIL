# 이진 파일 (binary file) : 글자가 아닌 비트 단위로 의미가 있는 파일
# - 그림 파일, 음악 파일, 동영상 파일, 엑셀 파일, 한글 파일, 실행(exe) 파일

# 텍스트 파일 : 메모장으로 열고 내용이 보이는 파일

# 이진파일 읽기
# open('이진파일이름', 'rb')
# read(1) : 1 바이트씩 읽기

# 이진파일 쓰기
# open('이진파일이름', 'wb')
# write()

# 이진파일 복사 (읽고 쓰기)
f1 = open('c:/windows/notepad.exe', 'rb')
f2 = open('c:/Temp/notepad.exe', 'wb')

while True:
    inStr = f1.read(1)
    if not inStr:       # 파일의 끝
        break
    f2.write(inStr)

f1.close()
f2.close()