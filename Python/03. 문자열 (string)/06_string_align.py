# 문자열 정렬 : 정렬 문자 <, >, ^
# 문자 : 왼쪽 정렬 / 숫자 : 오른쪽 정렬
# < : 왼쪽 정렬 / > : 오른쪽 정렬 / ^ : 가운데 정렬

string = 'python'
num = 1234
print(string)
print(num)

print('{:<10}' .format(string))
print('{:>10}' .format(string))
print('{:^10}' .format(string))

print('{:6d}' .format(num))       # 6자리로 만들어지고 숫자는 무조건 오른쪽 정렬
print('{:06d}' .format(num))      # 오른쪽 정렬하고 남은 부분은 0으로 채워짐

print('{:^10}' .format(string))
print('{:-<10}' .format(string))


# ljust() : 왼쪽 정렬
# rjust() : 오른쪽 정렬
# center() : 가운데 정렬
