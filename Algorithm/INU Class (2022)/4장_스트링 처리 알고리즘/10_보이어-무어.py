# 보이어-무어 스트링 탐색 프로그램

def index(c):
    if ord(c) == 32: return 0
    else: return ord(c) - 64

def initSkip(p):
    M = len(p)
    for i in range(NUM):
        skip[i] = M
    for i in range(M):
        skip[index(p[i])] = M - i - 1

def BM(p, t, k):
    M = len(p)
    N = len(t)
    initSkip(p)
    i = k + M -1
    j = M - 1
    global count
    if i >= N: return N
    while j >= 0:
        while t[i] != p[j]:
            s = skip[index(t[i])]
            if M - j > s: i += M - j
            else: i += s
            if i >= N: return N
            j = M - 1
        i -= 1
        j -= 1
        count += 1   # 비교할 때마다 횟수 추가
    return i + 1

NUM = 27
skip = [0] * NUM
text = 'STRING STARTING CONSISTING'
pattern = 'STING'
M = len(pattern)
N = len(text)
K = 0
count = 0         # 총 비교횟수 (전역변수로 선언)
while True:
    pos = BM(pattern, text, K)
    K = pos + M
    if K <= M: print('패턴이 나타난 위치 :', pos)
    else: break

print('총 비교횟수:', count)
print('스트링 탐색 종료')