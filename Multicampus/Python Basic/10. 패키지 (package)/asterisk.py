# * : 변수 앞에 붙은 경우 *args, **kwargs => 언패킹 (unpacking)

def asterisk_test1(a, *args) :
    print(a, args)
    print(type(args))

def asterisk_test2(a, *args) :
    print(a, *args)     # 튜플이나 리스트에 들어가 있는 것을 하나씩 펼쳐줌
    print(type(args))

asterisk_test1(1,2,3,4,5)
asterisk_test2(1,2,3,4,5)

# unpacking의 예시
# a, b, c = [1, 2, 3]
a, b, c = ([1, 2, 3], [3, 4, 5], [5, 6, 7])  # 길이가 같아야 함. 다르면 오류
print(a, b, c)
data = ([1, 2, 3], [3, 4, 5], [5, 6, 7])
print(*data)   # 요소 하나하나를 출력해줌

def asterisk_test3(a, **args):
    print(a, args)
    print(type(args))

asterisk_test3(1, b=2, c=3, d=4, e=5)

data2 = {'b':2, 'c':3, 'd':4, 'e':5}
asterisk_test3(1, **data2)