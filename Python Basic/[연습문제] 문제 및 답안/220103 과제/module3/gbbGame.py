from random import randint

you_n = ''

def gbb_game(you_n):
    com = randint(1, 3)
    if com - you_n == -2 or com - you_n == 1:
        result = '컴퓨터가 이겼습니다.'
    elif com - you_n == 0:
        result = '비겼습니다.'
    else:
        result = '당신이 이겼습니다'
    return result, com

def input_num():
    you_n = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    result, com = gbb_game(you_n)
    print(result)
    print('COM : {}' .format(com))
