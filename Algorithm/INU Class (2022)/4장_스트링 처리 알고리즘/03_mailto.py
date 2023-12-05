def bruteForce(p, t, k):
    M = len(p)  # 패턴의 길이
    N = len(t)  # 텍스트의 길이

    i = k
    j = 0
    global count

    while j < M and i < N:

        # 텍스트와 패턴이 같지 않을 때
        if t[i] != p[j]:
            i -= j
            j = -1
        
        # 텍스트와 패턴이 같을 때
        i += 1
        j += 1

        count += 1   # 비교할 때마다 횟수 추가

    if j == M: return i - M
    else: return i

text = open('email.html', 'r', encoding='UTF-8').read()
pattern = 'mailto:'
semi_pattern = '"'   # 쌍따옴표가 나올 때까지 text에 있는 문자 출력을 위함

M = len(pattern)  # 패턴의 길이
N = len(text)     # 텍스트의 길이
K = 0             # 탐색을 시작하는 위치
count = 0         # 총 비교횟수 (전역변수로 선언)

while True:
    pos = bruteForce(pattern, text, K)   # pos: 패턴이 나타난 위치
    K = pos + M
    
    # 탐색 위치가 텍스트 길이 안에 있을 때 if문 사용
    if K < N: 
        semi_pos = bruteForce(semi_pattern, text, K)
        print(text[pos+M:semi_pos])
    else: break