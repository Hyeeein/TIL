# 연습문제 4-1 (12월 23일 과제)
# 만든 날짜: 2021-12-23
# 만든이: 박혜인

e_mail = input('이메일 입력 : ')

jum_index = e_mail.find('.')
golbang_index = e_mail.find('@')

# 하나라도 만족하지 않으면 이메일 형식이 아니므로, 중첩 if문으로 만듦
# @ 또는 .이 없는 경우
if '@' not in e_mail or '.' not in e_mail:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

# @과 .이 위치가 바뀐 경우
elif jum_index < golbang_index:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

# @과 .사이에 문자가 없는 경우
elif jum_index - 1 == golbang_index:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

# @ 앞에 문자가 없는 경우
elif e_mail[golbang_index - 1].isalpha() == False:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

# . 뒤에 문자가 없는 경우
elif e_mail[jum_index + 1].isalpha() == False:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

# @또는 .이 두 번 이상 있는 경우
elif e_mail.count('@') >= 2 or e_mail.count('.') >= 2:
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일 :', e_mail)

else:
    print('입력한 이메일 형식이 맞습니다.')

## 피드백
# else - if 를 또 쓰는 것보단 elif를 사용하는 것이 더 나음


## 예시답안
# 여기서는 문자가 앞에 없는 경우는 숫자가 와도 상관없게 봄
#
# email = input('이메일 입력: ')
# if (email.find('@') == -1 or
#     email.find('.') == -1 or
#     email.index('@') > email.index(',') or
#     email.index('.') - email.index('@') < 2 or
#     email.index('@') == 0 or
#     len(email) - email.index('.') <= 1 or
#     email.count('@') >= 2 or
#     email.count('.') >= 2) :
#     print('이메일의 형식이 아닙니다')
#
# print('입력한 이메일 %s' % email)
