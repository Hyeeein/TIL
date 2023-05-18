# 예제.

# def sub(x, y):
# #    global a
#     a=7     # 전역변수
#     x, y = y, x     # x, y: 지역변수
#     b=3     # 지역변수
#     print('sub()------')
#     print(a,b,x,y)
#     print('sub()_a: ',id(a))
#     print('sub()_b: ',id(b))
#     print('sub()_x: ',id(x))
#     print('sub()_y: ',id(y))
#     print('------------')
#
# a,b,x,y=1,2,3,4
# sub(x,y)
# print('a: ', id(a))
# print('b: ', id(b))
# print('x: ', id(x))
# print('y: ', id(y))
# print(a,b,x,y)

# a=1  # 함수 밖에서 정의된 전역변수 a

# def show():
#     print('show() 함수')
#     print(a) # 전역변수 a
#     print(id(a))
#     print('---------')
#
# show()
# print(a)
# print(id(a))
#
def show(a):    # a : 매개변수 => 함수 내부에서 지역변수로 사용
    a=a+1
    print('show() 함수')
    print(a)
    print(id(a))

show(10)
# print(a)