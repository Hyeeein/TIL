# 3. 회원명단 파일 작성 및 명단 파일 읽기

def input_member(infile):
    with open(infile, 'w', encoding='utf-8') as f:
        while True:
            member = input('멤버를 입력하세요.(종료는 q) : ')
            if member == 'q':
                break
            else:
                f.write(member+'\n')

def output_member(outfile):
    with open(outfile, 'r', encoding='utf-8') as f:
        print(f.read())

while True:
    opt = input("저장 1, 출력 2, 종료 q : ")
    if opt =='1':
        infile = input('멤버명단을 저장한 파일명을 입력하세요 : ')
        input_member(infile)
    elif opt=='2':
        outfile = input('멤버명단이 저장된 파일명을 입력하세요 : ')
        output_member(outfile)
    elif opt == 'q':
        break
    else:
        print('잘못입력하셨습니다')

# 윤형석 작성
def input_member(fn):
    f = open(fn, 'a')
    while True:
        name = input('멤버를 입력하세요 (종료는 q):')
        if name == 'q':
            break
        data=name +'\n'
        f.write(f'{name}\n')
    f.close()

def output_member(fn):
    try:
        f=open(fn,'r')
    except FileNotFoundError:
        print('파일이 없습니다.')
    else:
        while True:
            line= f.read()
            if not line:
                break
            print(line)
        f.close()

while True:
    num = input('저장 1,출력 2, 종료 q : ')
    if num=='1':
        filename= input('멤버 명단을 저장할 파일명 :')
        input_member(filename)

    elif num=='2':
        filename = input('멤버 명단 파일명 :')
        output_member(filename)

    elif num=='q':
        break