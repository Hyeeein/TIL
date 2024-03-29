# 알고리즘
# insert(a[], v)
#     x <- hash(v);
#     while (a[x] != -1) do
#         x <- (x + 1) % M;
#     a[x] <- v;
# end insert()

# search(a[], v)
#     x <- hash(v);
#     while (a[x] != -1) doc
#         if (v == a[x]) then
#             return a[x];
#         else (x <- (x + 1) % M);
# end search()

# hash(v)
#     return v mod M;
# end hash()

# 프로그래밍
class Dict:
    def __init__(self):
        Dict.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            x = (x + 1) % M
        Dict.a[x] = v

    def search(self, v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]
            else:
                x = (x+1) % M
        return -1

    def hash(self, v):
        return v % M

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
print('선형 탐사법의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')