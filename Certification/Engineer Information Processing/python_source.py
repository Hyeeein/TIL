# 1번
a = {'일본', '중국', '한국'}
a.add('베트남')
a.add('중국')
a.remove('일본')
a.update({'홍콩', '한국', '태국'})
print(a)

# 2번
lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])
print(lol[2][1])
for sub in lol:
    for item in sub:
        print(item, end='')
    print()

# 3번
class Soojebi:
    li = ["Seoul", "Kyeonggi", "Incheon", "Daejeon", "Daegu", "Pusan"]

s = Soojebi()
str01 = ''
for i in s.li:
    str01 = str01 + i[0]

print(str01)

# 4번
a = 100
i = 0
result = 0
for i in range(1, 3):
    result = a >> i
    result += 1

print(result)

# 5번
a, b = 100, 200
print(a==b)

# 6번
a = "Hello Python"
b = a[0:3]
c = a[-4:-1]
print(b+c)

# --------
# 7번
a = 5
for i in range(1, a+1):
    if a % i == 0:
        print(i)

# 8번

# 9번

# 10번

# 11번

# 12번

# 13번

# 14번

# 15번

# 16번

# 17번

# 18번

# 19번

# 20번

# 21번

# 22번

# 23번

# 24번