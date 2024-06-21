# 예외 (Exception) : 오류에 대처하기 위한 오류
# 예외 처리 : 오류 발생 시 프로그램이 중단되고 에러 메시지가 출력되지 않도록 예외를 발생시켜
#           프로그램이 정상 작동하도록 하는 것. 즉 에러 종류와 상관없이 예외 처리 함

# 참고 홈페이지 : https://docs.python.org/ko/3/library/exceptions.html

# 예외 처리 형식 : try ~ except 문 사용
# try:
#     에러가 발생할 문장들
# except :
#     에러가 발생하면 처리하는 코드들
# else:
#     에러가 발생하지 않으면 처리하는 문장
# finally:
#     에러와 상관없이 항상 수행하는 문장


# 에러의 종류와 상관없이 에러를 처리하는 경우
## 예제. 0으로 나누는 경우 처리
try:
    print(10/0)
except:
    # print('0으로 나눌 수 없습니다')
    print('오류발생')

# 에러 종류 명시 처리
try:
    print(10/0)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다')

# ValueError
try:
    num = int(input('숫자를 입력하세요'))
except ValueError:
    print('숫자가 아닙니다.')


# 여러 가지 예외를 같이 처리할 수 있음
# 방법 1
try:
    print(10/0)
    print('나이 : ' + 23 + '살')
except (ZeroDivisionError, TypeError) as e:      # 에러 메시지 변수
    print('0으로 나눌 수 없습니다', e)
except TypeError as e:
    print('형식이 잘못 지정되었습니다.', e)

# 방법 2
try:
    print(10/0)
    print('나이 : ' + 23 + '살')
except (ZeroDivisionError, TypeError) as e:      # 에러 메시지 변수
    print('오류가 발생했습니다.', e)

# 방법 3
try:
    f = open('text.txt', 'r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('End ----- ')