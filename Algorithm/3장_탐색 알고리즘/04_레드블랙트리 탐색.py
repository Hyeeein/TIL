# 알고리즘
# black ← 0;
# red ← 1;
# insert(T, v)

#     // p : x의 부모 노드, g : x의 조부모 노드, gg : x의 증조부모 노드
#     x ← T;
#     p ← T;
#     g ← T;
#     while (x ≠ null) do {
#         gg ← g;
#         g ← p;
#         p ← x;
#         if (x.key = v) then return;
#         if (x.key > v) then x ← x.left;
#         else x ← x.right;
#         if ((x.left.color = red) and (x.right.color = red)) then
#             split(x, p, g, gg, v);
#     }
#     x ← color가 red이고 key 값이 v인 새로운 노드;
#     if (p.key > v) then p.left ← x;
#     else p.right ← x;
#     split(x, p, g, gg, v);
# end insert()

# split(x, p, g, gg, v)
#     x.color ← red;
#     x.left.color ← black;
#     x.right.color ← black;
#     if (p.color = red) then {
#         g.color ← red;
#         if ((g.key > v) ≠ (p.key > v)) then
#             p ← rotate(v, g);
#         x ← rotate(v, gg);
#         x.color ← black;
#     }
# end split()

# rotate(v, y)
#     // c : y의 자식 노드, gc : y의 손주 노드
#     c ← y;
#     gc ← y;
#     if (y.left.color = red) then c ← y.left;
#     else then c ← y.right;
#     if (c.left.color = red) then gc ← c.left;
#     else then gc ← c.right;
    
#     //왼쪽 단일 회전일 경우
#     if ((y.left = c) and (c.left = gc)) then {
#         c.left ← gc.right;
#         gc.right ← c;
#         y.left ← gc;
#     }
#     //오른쪽 단일 회전일 경우
#     if ((y.right = c) and (c.right = gc)) then {
#         c.right ← gc.left;
#         gc.left ← c;
#         y.right ← gc;
#     }
#     //왼-오 이중 회전일 경우
#     if ((y.left = c) and (c.right = gc)) then {
#         c.right ← gc.left;
#         gc.left ← c;
#         y.left ← gc;
#     }
#     //오-왼 이중 회전일 경우
#     if ((y.right = c) and (c.left = gc)) then {
#         c.left ← gc.right;
#         gc.right ← c;
#         y.right ← gc;
#     }    
#     return gc;
# end rotate()

# 프로그래밍
black = 0
red = 1

class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right

class Dict:
    z = node(color=black, key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(color=black, key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right
        while (x != self.z):
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1

    def insert(self, v):
        x = p = g = self.head
        while (x != self.z):
            gg = g
            g = p
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)
                
        x = node(color=red, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black
        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black

    def rotate(self, v, y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right
        
        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc

    def check(self, search_key):    
        x = self.head.right
        cur = x
        while (x != self.z):

            if x.key > search_key:
                if(x.color):
                    print('key : ', x.key, ', parents : ', cur.key, ', color : red')
                else:
                    print('key : ', x.key, ', parents : ', cur.key, ', color : black')
                cur = x
                x = x.left
            else:
                if(x.color):
                    print('key : ', x.key, ', parents : ', cur.key, ', color : red')
                else:
                    print('key : ', x.key, ', parents : ', cur.key, ', color : black')
                cur = x
                x = x.right
        return -1


# import random, time

# N = 10000
# key = list(range(1,N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)

# d = Dict()
# for i in range(0, N):
#     d.insert(key[i])
# start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end_time = time.time() - start_time
# print('레드 블랙 트리 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')


d = Dict()
key = int(input('키: '))
while key != 999:
    d.insert(key)
    d.check(key)
    key = int(input('키: '))
