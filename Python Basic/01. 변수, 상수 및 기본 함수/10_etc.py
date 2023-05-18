# 입력 내용이 길어서 여러 줄에 작성해야 하는 경우
sum1 = 1 + 2 + 3 + 4 + \
    5 + 6 + 7

sum2 = (1 + 2 + 3 + 4 +
       5 + 6 + 7)

# 3줄로 써도 이건 1줄로 인식
print("긴문장으로 표현"
      "두 번째"
      "세 번째")

# 여러 줄로 출력
# \n : 줄바꿈
print("긴문장으로 표현\n두 번째\n세 번째\n")

# 특수문자 있는 그대로 사용하고 싶을 때는 앞에 \ (escape)을 사용
# \n : 줄바꿈
# \t : tab (일정한 간격)
# \' : '
# \" : "
# \\ : \

print('don\'t')
print('123\t 456')
print('He said, \'yes\'')
print('He said, "yes"')

# escape 의미를 제거 : r
print('c:\pythonStury\day2')
print(r'c:\pythonStudy\name')

# 2개의 명령어(문장)을 한 줄에 입력 : ; (세미클론) 또는 end 사용
print(sum1) ; print(sum2)

print('apple', end = '')
print('banana', end = '$')
print('melon')

# 한 개의 문장을 여러 줄에 출력
print('apple \n banana \n melon')
print('apple')
print('banana')
print('melon')