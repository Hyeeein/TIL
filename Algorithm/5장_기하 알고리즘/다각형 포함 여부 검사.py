import geo as g
import sys

def ccw(p0, p1, p2):
    pass

def intersect(l1, l2):
    t1 = ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)
    t2 = ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)
    return t1 <= 0 and t2 <= 0

def theta(p1, p2):
    pass

def selectionSort(p, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1):
            if theta(p[1], p[j]) < theta(p[1], p[minIndex]):
                minIndex = j
        p[minIndex], p[i] = p[i], p[minIndex]

def inside(t, p, n):
    count, j = 0, 0
    lt, lp  = g.line(), g.line()
    p[0], p[n+1] = p[n], p[1]
    lt.p1 = t
    lt.p2.x = sys.maxsize
    lt.p2.y = t.y
    for i in range(1, n+1):
        lp.p1, lp.p2 = p[i], p[i]
        # 코드 추가
        if ():
            lp.p2 = p[j]
            j = i
            if ():
                count += 1

    return count % 2

def printInside(t, res):
    print('점 (%s, %s) :'%(t.x, t.y), end=' ')
    if res:
        print('내부')
    else:
        print('외부')

N = 16
t = g.point(None, None, None)
p = []
p.append(g.point(None, None, None))
for i in range(N):
    p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))
p.append(g.point(None, None, None))
minIndex = 1
for i in range(2, N+1):
    if p[i].y < p[minIndex].y:
        minIndex = i
p[minIndex], p[1] = p[1], p[minIndex]
selectionSort(p, N)