# 상품 가격, 주문 수량을 입력받아서 주문액을 계산하여 반환하는 함수 작성
# 함수명 : order()

# 상품가격 입력 : 1000
# 주문수량 입력 : 10
# ---------------------
# 상품가격 : 1000원
# 주문수량 : 10개
# 주문액 : 10000원

def order():
    price = int(input('상품가격 입력: '))
    qt = int(input('주문수량 입력: '))
    amount = price * qt
    return price, qt, amount

# price, qty, amount = order()

# print('-------------')
# print('상품가격 : %d원' % price)
# print('주문수량 : %d개' % qty)
# print('주문액 : %d원' % amount)

result = order()
print(result)
print('-------------')
print('상품가격 : %d원' % result[0])
print('주문수량 : %d개' % result[1])
print('주문액 : %d원' % result[2])

