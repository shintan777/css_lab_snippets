"""
Basic rsa algorithm with encryption and decryption
"""
from math import gcd, pow


def inverse(p, n):
    """
    Returns modular inverse of p in mod n
    """
    p %= n
    for i in range(2, n):
        if (p*i) % n == 1:
            return i

    return 1


def coprime(x):
    """
    Returns a coprime of x
    """
    for i in range(2,x):
        if(gcd(x, i) == 1):
            return i

    raise ValueError("Cannot find coprime of {}".format(x))


def decrypt(e, phi):
    for i in range(1, e):
        x = 1 + i*phi
        if x % e == 0:
            d = int(x/e)
            return d


def calc_keys(p, q):
    try:
        n = p * q
        phi = (p-1) * (q-1)
        e = coprime(phi)
        d = inverse(e, phi)
    except Exception as e:
        print(e)

    return e, d, phi, n


p, q = map(int, input("Enter 2 prime nos. (space separated)").split())
e, d, phi, n = calc_keys(p, q)
print("public key is {} and private key is {}".format(e, d))
while True:
    opt = input("Enter 1 for ecryption 2 for decrytion and 3 for exit\n")
    if opt == '1':
        s = input("Enter number as a message\n")
        m = int(s)
        c = int(pow(m, e) % n)
        print("Cipher text\n", str(c))
    elif opt == '2':
        s = int(input("Enter Cipher text\n"))
        d = int(pow(s, d) % n)
        print("Plain text\n", str(d))
    elif opt == '3':
        break
    else:
        print("Enter correct input\n")
