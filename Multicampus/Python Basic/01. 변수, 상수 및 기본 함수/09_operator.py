# 산술연산자 : 지수는 여기서 **을 사용 (^을 사용하면 오류)

## 연습문제 1 : 현금 5000원, 사탕 가격 120원일 때 최대한 살 수 있는 사탕의 개수와 나머지 돈은?

myMoney = 5000
candyPrice = 12
numCandies = myMoney // candyPrice
change = myMoney % candyPrice

print("사탕의 개수: %d개" % numCandies)
print("나머지 돈: %d원" % change)

# print("사탕의 개수 : {}개" .format(numCandies))
# print("잔돈 : {}원" .format(change))

# 연산자 우선순위 : 괄호 () > 지수 ** > 곱셈 *, 나눗셈 /, 나머지 % > 덧셈 +, 뺄셈 -

# 관계연산자 : >, <, >=, <=, ==, !=
# 논리연산자 : and, or, not

a = 15
print(a > 10 and a < 20)
print((a % 3 == 0) or (a % 7 == 0))
print(not(a == 100))

# 비트연산자: 비트가 가지고 있는 1, 0의 개념을 가지고 논리곱을 하는 것