scan = -1

# (A*B+AC)D
ch = [' ', 'A', ' ', 'B', ' ', ' ', 'A', 'C', 'D', ' ']
next1 = [5, 2, 3, 4, 8, 6, 7, 8, 9, 0]
next2 = [5, 2, 1, 4, 8, 2, 7, 8, 9, 0]

class Deque:
    def __init__(self, size):
        self.deque = []
        self.first = int(size/2)
        self.last = int(size/2)
        for i in range(size):
            self.deque.append(0)

    def insertFirst(self,v):
        self.deque[self.first] = v
        self.first -= 1

    def insertLast(self, v):
        self.last += 1
        self.deque[self.last] = v

    def deleteFirst(self):
        self.deque[self.first] = 0
        self.first += 1
        return self.deque[self.first]

    def isEmpty(self):
        if self.first == self.last:
            return True
        else:
            return False

    def checkDq(self):
        if self.deque[self.first] == 0:
            if self.last - self.first < 2 and self.deque[self.last] == scan:
                return False
            elif not self.isEmpty():
                return True
            else:
                return False
        else:
            return False

    def prDq(self, size):
        pass


def match(t):
    pass

text = 'AABD' + '\0'
#text = 'CDAABCAAABD' + '\0'
previous = 0
i = 0
N = len(text)-1
while True:
    pos = match(text[i:])
    if pos <= 0:
        break
    pos += previous
    i = pos
    if i <= N:
        print('패턴이 나타난 위치 : ', pos)
    else:
        break
    previous = i
print('패턴 매칭 종료')