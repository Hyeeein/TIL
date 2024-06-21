# 헷갈리시는 분들은 이렇게 외우세요.
# print(id(x))
# print(id(y))
# id 값이 변경되면 immutable / 변경되지 않으면 mutable


# 수치형, 문자열 변경 불가능 (immutable)
x = '123'
y = x
y += '4'
print(x)
print(y)

# 튜플은 변경 불가능(immutable)
x = (1, 2)
y = x
y = y + (3,)
print(x)
print(y)

# 리스트는 변경 불가능(immutable)
x = [1, 2]
y = x
y.append(3)
print(x)
print(y)

# 딕셔너리는 변경가능(mutable)
x = {1:2}
y = x
y[2] = 3
print(x)
print(y)