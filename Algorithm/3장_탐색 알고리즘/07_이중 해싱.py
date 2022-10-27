# 알고리즘
# insert(a[], v)
#     x <- hash(v);
#     u <- hash2(v);
#     while (a[x] != -1) do
#         x <- (x + u) % M;
#     a[x] <- v;
# end insert()

# search(a[], v)
#     x <- hash(v);
#     u <- hash2(v);
#     while (a[x] != -1) do
#         if (v == a[x]) then
#             return a[x];
#         else (x <- (x + u) % M);
# end search()

# hash(v)
#     return v mod M;
# end hash()

# hash2(v)
#     return 64 - (v mod 64);
# end hash2()


# 파이썬 프로그래밍
class Dict:
    def __init__(self):
        Dict.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while Dict.a[x] != -1:
            x = (x + u) % M

    def search(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]
            else:
                x = (x + u) % M
        return -1

    def hash(self, v):
        return v % M

    def hash2(self, v):
        return 64 - (v % 64)

import random, time

N = 10000
M = 10391
key = []
s_key = []
for i in range(N):
    r = random.randint(1, 3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.clock()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('탐색 오류')
end_time = time.clock() - start_time
print('이중 해싱의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')