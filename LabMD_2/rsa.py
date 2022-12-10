
def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


def is_coprime(a, b):
    if gcd(a, b) == 1:
        return 1
    return 0


def get_modular_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return 0


def get_e(p, q):
    for x in range(2, phi):
        if is_coprime(x, phi):
            return x
    return "Error"


# Starting data
decrypted = 95384
p = 281
q = 283
n = p * q
phi = (p - 1) * (q - 1)

# Calculated data
e = get_e(p, q)
d = get_modular_inverse(e, phi)
encrypted = pow(decrypted, e) % n
decrypted = pow(encrypted, d) % n

# Output
print("=================")
print("Public key:")
print((n, e))
print("=================")
print("Private key:")
print((n, d))
print("=================")
print("Initial message:")
print(decrypted)
print("=================")
print("Encrypted message:")
print(encrypted)
print("=================")
print("Decrypted message:")
print(decrypted)
print("=================")
