def encipher(plain, n, p):
    cipher = ''
    i = 0
    while i < len(plain):
        m = ''
        for j in range(4):
            m += plain[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(p):
            b = t % n
            t = a * b
        if b < 10:
            cipher += '000' + str(b)
        elif b < 100:
            cipher += '00' + str(b)
        elif b < 1000:
            cipher += '0' + str(b)
        else:
            cipher += str(b)
    return cipher

def encode(plain):
    n = len(plain)
    m = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32: a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)
    return m

def decipher(p, n, pk):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        b = 0
        for k in range(pk):
            b = t % n
            t = a*b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)

    return c

def decode(p):
    m = ''

    for i in range(0, len(p), 2):
        a = int(p[i:i+2]) + 64
        if a == 64:
            a = 32
        m += chr(a)

    return m

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97
P = 37
plainMessage = encode(plainText)
print('평  문 : ', plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print('암호문 : ', cipherMessage)
decodeMessage = decipher(cipherMessage, N, S)
print("복호문 : ", decodeMessage)
decodeText = decode(decodeMessage)
print("복호문 : ", decodeText)
print("복호문 길이 : ", len(decodeText))