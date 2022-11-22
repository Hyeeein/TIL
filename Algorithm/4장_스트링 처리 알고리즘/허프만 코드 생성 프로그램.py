class PQ:
    def __init__(self):
        self.heap = [0]*100
        self.info = [0]*100
        self.n = 0

    def insert(self, v, x):
        self.n += 1
        i = self.n
        while True:
            if i == 1: break
            if v >= self.heap[int(i/2)]: break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]: break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0: return True
        else: return False

def index(c):
    if ord(c) == 32: return 0
    else: return (ord(c)-64)

def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1

    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)

    i = 27
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty():
            pq.insert(count[i], i)
        i += 1
    
    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
        code[k] = x
        length[k] = i
    
    # count, dad, code, length 리스트의 0 제거
    # remove는 해당하는 값 하나만 지워지므로 while문으로 작성해줌
    while 0 in count:
        count.remove(0)
    
    while 0 in dad:
        dad.remove(0)
    dad.append(0)  # dad 리스트 맨 마지막에 0 추가

    '''
    while 0 in code:
        code.remove(0)
    code.insert(11, 0)  # code 리스트 N 자리에 0 삽입
    
    while 0 in length:
        length.remove(0)

    근데 이 코드들을 넣으면 인코딩이 안됨...
    '''

    # count[k] 출력 코드 추가
    print('count[k]:', count[0:44])
    print()

    # dad[k] 출력 코드 추가
    print('dad[k]:', dad[0:44])
    print()

    # code[k] 출력 코드 추가
    print('code[k]:', code)
    print()

    # length[k] 출력 코드 추가
    print('length[k]:', length)
    print()

def encode(t, m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1
    return huffman_code

def char(k):
    if k == 0: return chr(32)
    else: return chr(k+64)

# 부모 노드를 찾아내는 함수
def findDad(max_i, k):
    for i in range(max_i):
        if dad[i] == k:
            return i

# 디코딩 하는 함수
def decode(h):           # h는 변환된 이진수들
    decoding_text = ""   # 디코딩 된 문자열

    # 이진수를 리스트 안에 숫자 형태로 바꿔서 저장
    encoding_text = []
    for i in range(len(h)):
        encoding_text.append(int(h[i]))

    # 저장된 이진수 왼쪽부터 순차적으로 진행 (리스트 끝날 때까지)
    i = 0
    k_list = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 15, 16, 18, 19, 20, 21,
              27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
    k = k_list[findDad(35, encoding_text[0])]  # 초기 값 세팅

    while i < len(encoding_text):

        # 이진수가 1일 경우, 마이너스 부호를 붙여줌
        if encoding_text[i] == 1:
            k = -k
        
        k = k_list[findDad(35, k)]

        # k값이 22이하, 즉 알파벳으로 바뀔 수 있으면 바꿔서 저장
        # 이때, dad[k]의 길이가 35이므로, max_i는 35
        if 0 <= k < 22:
            decoding_text += char(k)
            
            # 1이 연속으로 3개 -> 띄어쓰기 (리스트 범위 넘어가게 비교하지 X)
            if i < len(encoding_text)-2 and encoding_text[i+1] == 1:
                if encoding_text[i+2] == 1:
                    if encoding_text[i+3] == 1:
                        decoding_text += char(0)
                        i += 3

            # k값 초기화
            k = 43

        i += 1

    return decoding_text  

# text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [0]*100
dad = [0]*100
length = [0]*27
code = [0]*27
M = len(text)
pq = PQ()
makeHuffman(text, M)
h = encode(text, M)
print('<인코딩 결과>')
print(h)
print()
d = decode(h)
print('<디코딩 결과>')
print(d)