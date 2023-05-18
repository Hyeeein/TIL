## 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():     # pop이랑 비슷한데 peek은 다음에 누가 나올지 미리 말해주는 용도
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피1')
push('커피2')
# push('커피3')
# push('커피4')
# push('커피5')
print(stack)
# push('커피6')

print('다음 예정 --->', peek())

retData = pop()
print('팝 --->', retData)
retData = pop()
print('팝 --->', retData)
retData = pop()
print('팝 --->', retData)

print(stack)