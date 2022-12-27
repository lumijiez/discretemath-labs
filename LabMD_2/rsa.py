class RSA:
    def __init__(self):
        self.e = self.d = self.p = self.q = self.phi = 0

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __modinv(self, a, m):
        g, x, y = self.__egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def encrypt(self, m, keyPair=None):
        if (keyPair == None):
            keyPair[0] = self.e
            keyPair[1] = self.n

        return pow(m, keyPair[0], keyPair[1])

    def decrypt(self, c, keyPair=None):
        if (keyPair == None):
            keyPair[0] = self.d
            keyPair[1] = self.n

        return pow(c, keyPair[0], keyPair[1])

    def generateKeys(self, p, q, e=3):
        self.p = p
        self.q = q

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = e
        self.d = self.__modinv(self.e, self.phi)

        if (self.phi % self.e == 0):
            raise Exception('invalid values for p and q')

    def getPublicKey(self):
        return self.e, self.n

    def getPrivateKey(self):
        return self.d, self.n


letterHashmap = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 36
}

letterHashmapReverse = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q',
    27: 'R',
    28: 'S',
    29: 'T',
    30: 'U',
    31: 'V',
    32: 'W',
    33: 'X',
    34: 'Y',
    35: 'Z',
    36: ' '
}


def hashMessage(msg, init):
    hashedMessage = letterHashmap[init]
    for x in range(1, len(initialMessage)):
        hashedMessage = hashedMessage * 100 + letterHashmap[initialMessage[x]]
    return hashedMessage


def unhashMessage(msg):
    letters = []
    while msg > 10:
        if msg % 100 in letterHashmapReverse:
            letters.append(letterHashmapReverse[msg % 100])
        msg = msg // 100
    strn = ''.join(letters)
    strn = strn[::-1]
    return strn


rsa = RSA()
rsa.generateKeys(
    17055899557196527525682810191339089909014331959812898993437334555169285087976951946809555356817674844913188193949144165887100694620944167618997411049745043243260854998720061941490491091205087788373487296637817044103762239946752241631032791287021875863785226376406279424552454153388492970310795447866569138481,
    171994050316145327367864378293770397343246561147593187377005295591120640129800725892235968688434055779668692095961697434700708550594137135605048681344218643671046905252163983827396726536078773766353616572531688390937410451433665914394068509329532352022301339189851111636176939179510955519440490431177444857017)

initialMessage = "i love math".upper()
message = hashMessage(initialMessage, initialMessage[0])

encrypted = rsa.encrypt(message, keyPair=rsa.getPrivateKey())
decrypted = rsa.decrypt(encrypted, keyPair=rsa.getPublicKey())

print(initialMessage)
print(message)
print(encrypted)
print(decrypted)
print(unhashMessage(decrypted))
