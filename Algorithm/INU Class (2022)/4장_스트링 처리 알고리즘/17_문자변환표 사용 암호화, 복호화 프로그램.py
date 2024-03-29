def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32:
            a = 0
        else:
            a -= 64
        cipher += k[a]
    return cipher

def decipher(cipher, k):
    decipherText = ''
    for i in cipher:
        a = k.index(i)
        if a == 0:
            a = 32
        else:
            a += 64
        decipherText += chr(a)
    return decipherText

plainText = 'SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평  문 : ', plainText)
cipherText = encipher(plainText, K)
print('암호문 : ', cipherText)
decipherText = decipher(cipherText, K)
print('복호문 : ', decipherText)