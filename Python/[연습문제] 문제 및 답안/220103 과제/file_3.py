# 문제 3 : 회원 명단 출력 프로그램
# 만든 날짜 : 2022-01-03
# 만든이 : 박혜인

# 회원 명단을 입력 받아 파일로 저장하는 함수
def input_member(f1):
    f1 = open(file_input, 'w', encoding='utf-8')
    while True:
        member = input('멤버를 입력하세요. (종료는 q) : ')
        if member == 'q':
            break
        f1.write(member)
        f1.write('\n')

# 사용자가 입력한 파일을 열어서 출력해주는 함수
def output_member(f2):
    f2 = open(file_output, 'r', encoding='utf-8')
    names = f2.readlines()

    for name in names:
        print(name, end='')

# main 함수
while True:
    n = input('저장 1, 출력 2, 종료 q : ')

    if n == 'q':
        break

    elif n == '1':
        file_input = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(file_input)

    elif n == '2':
        file_output = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(file_output)

    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요.')