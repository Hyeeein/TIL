# for 문: 정해진 횟수만큼 반복

# for 변수 in 리스트 또는 범위 :
#     반복 문장 1
#     반복 문장 2
#     ...

for name in ['apple', 'banana', 'melon']:
    print(name)

# range(끝값 + 1) : 0 ~ 끝값까지
# range(시작값, 끝값 + 1) : 시작값부터 끝값까지
# range(시작값, 끝값 + 1, 간격) : 시작값부터 끝까지 그 간격만큼 띄워서 반복

for number in range(10):  # 0 ~ 9까지
    print(number)

for number in range(1, 10):  # 1 ~ 9까지 (시작값, 끝값+1)
    print(number)

for number in range(1, 10, 2):
    print(number)

# range(1, 10, 2)을 리스트로 써보기
for number in [1, 3, 5, 7, 9]:
    print(number)

# -----------

# 중첩 for

for y in range(3):
    print(y)
    for x in range(5):
        print(x, end=' ')
    print() # 띄워쓰는 용도

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

num = 0
for y in range(3):
    for x in range(4):
        num += 1
        print(num, end=' ')
    print()

n = 1
for i in range(3):
   for i in range(n, n+4):
       print(i, end=' ')
   print()
   n+=4

n=0
for y in range(3) :
    for x in range(1,5) :
        print(n+x, end=' ')
    n += 4
    print()

for y in range(3):
    for x in range(1, 5):
        print(x + y * 4, end = ' ')
    print()

for y in range(1,13,4):
  for x in range(4):
    print(y+x, end=' ')
  print()