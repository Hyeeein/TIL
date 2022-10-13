class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node

    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)
            

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if search_key == x.key:
                return x.key
            if search_key > x.key:
                x=x.right
            else:
                x=x.left
        return -1

    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

    def check(self, search_key):
         if search_key<11:
             print("key :",search_key,end=" ")
         x = p = self.head.right
         
         while x.key != search_key:
             p=x
             if x.key < search_key:
                 x = x.right
             else:
                 x = x.left
         if search_key<11:
             print("parents :",p.key)
            
                

import random, time
N = 100000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])
#for i in range(1,N+1):
#    d.insert(i)
for i in range(1,N+1):
    d.check(i)
start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time
print('이진 트리 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')
