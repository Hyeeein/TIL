# 리스트의 요소 제거

# remove(값) : 지정한 값을 제거, 동일한 값은 한번에 제거할 수 없고 제일 처음 만나는 값만 제거
# pop() : 마지막의 요소 값을 제거
# pop(index) : index 위치 요소값을 제거

x = ['apple', 'banana', 'coconut', 'banana', 'melon']
print(x)

x.remove('melon')
print(x)

x.remove('banana')   # 동일한 값이 두 번 이상 나올 경우, 처음 나오는 'banana'를 지움
print(x)

# 다 지우고 싶을 경우 for문을 사용하여 지움
n = x.count('banana')
for i in range(n):
    x.remove('banana')
print(x)

y = [1, 3, 5, 1, 10]
last = y.pop()
print(y)
print(last)
y.append(-10)
print(y)
rm = y.pop(3)
print(y)
print(rm)
# y.remove(0)

y[3] = 'list'
print(y)