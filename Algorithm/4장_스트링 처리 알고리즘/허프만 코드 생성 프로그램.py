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
def decode(h):  # h는 변환된 이진수들
    
    # 이진수를 리스트 안에 저장
    d_tmp = []
    for i in range(len(h)):
        d_tmp.append(h[i])

    # 저장된 이진수 왼쪽부터 순차적으로 진행
    for i in d_tmp:
        
    
    # dad[k]가 0인 k를 찾으면 43

    # 1이니까 dad[k]를 음수로 바꾸고 -43인 것을 찾으면 42

    # 1이니까 dad[k]를 음수로 바꾸고 -42인 것을 찾으면 40

    # 0이니까 dad[k]가 40인 것을 찾으면 36

    # dad[k]가 36일 때, k는 5 => 알파벳 E

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
print(h)
d = decode(h)
print(d)