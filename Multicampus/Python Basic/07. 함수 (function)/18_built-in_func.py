# iterable (반복 가능한 자료형) : 리스트, 튜플, 딕셔너리
# for 반복문을 이용해서
print('all()-------')
print(all([1, 2, 3]))
print(all([0, 2, 3]))

# any() : 하나라도 참이면 True
print('any()-------')
print(any([1, 2, 3]))
print(any([0, 2, 3]))
print(any([0, 0, 0]))
print(any([0, "", 0]))  # 빈문자열 "" : False
print(any([0, "", []])) # 빈 리스트[] : False

# bool()
print(bool(""))
print(bool([]))
print(bool(1))
print(bool(10))
print(bool(-10))
print(bool({}))
print(bool(None))

# chr() : 아스키코드(ASCII) 값에 해당하는 문자 반환
print("chr()-------")
print(chr(95))
print(chr(97))
print(chr(65))
print(chr(55))

# ord() : 문자에 대한 ASCII 코드 값 반환
print("ord()--------")
print(ord('A'))
print(ord(' '))
print(ord('\n'))
print(ord('\t'))
print(ord('0'))

# divmod(a, b) : a를 b로 나눈 몫과 나머지 반환
print("div()--------")
print(divmod(10, 3))    # 반환 값은 튜플형태 (몫, 나머지)

# enumerate() : 시퀀스의 각 값에 인덱스를 포함해서 enumerate 객체로 변환
# 시퀀스 : range(), 문자열, 리스트, 튜플, ...
print("enumerate()-------")
print(enumerate('hello'))
for i, c in enumerate('hello'):
    print(i, c)
for i, season in enumerate(['봄', '여름', '가을', '겨울']):
    print(i, season)

# eval() : 표현식의 연산 결과 반환
print("eval()-------")
print(eval('1+2'))
print(type(eval('10')))
x = 1
print(eval('x+1'))

# filter(function, iterable) : iterable 자료의 요쇼들을 function으로 거르다(걸러내다)
print("filter()--------")

def positive(x):
    return x > 0

print(filter(positive, [0, 1, -1, 10, -3, 5]))
# positive 함수로 걸러낸 객체 반환
print(list(filter(positive, [0, 1, -1, 10, -3, 5])))

def even(x):
    if x % 2 == 0:
        return x

print(list(filter(even, [0, 1, -1, 10, -3, 5])))

# help() : 도움말
help(print)
help(filter)
help(input)
help(max)

# pow(x, y) : x의 y 제곱
print(pow(10, 3))
print(pow(2, 10))

# range([start], stop [, step]) : 지정한 범위의 값을 반복 가능한 객체로 반환
print(range(0, 5))
print(list(range(0, 5)))

# zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(zip([1, 2, 3], [4, 5, 6]))
print(list(zip[1, 2, 3], [4, 5, 6]))
print(list(zip[1, 2, 3], [4, 5, 6], [7, 8, 9]))

keys = ['apple', 'melon', 'banana']
vals = [250, 300, 400]

print(list(zip(keys, vals)))
print(dict(zip(keys, vals)))