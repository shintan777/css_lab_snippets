"""
Basic rsa algorithm with encryption and decryption
"""
from math import gcd, pow


def inverse(p,n):
    """
    Returns modular inverse of p in mod n
    """
    for i in range(2,p):
        if (p*i)%n == 1:
            return i

    raise ValueError("No inverse exists")

def coprime(x):
    for i in range(2,x):
        if(gcd(x,i)==1):
            return i

    raise ValueError("Cannot find coprime of {}".format(x))

def calc_keys(p, q):
    try:
        n = p * q
        phi = (p-1) * (q-1)
        e = coprime(phi)
        d = inverse(e,n)
    except Exception as e:
        print(e)

    return e, d, phi

p, q = map(int, input("Enter 2 prime nos. (space separated)").split())
e, d, phi = calc_keys(p, q)
print("public")
opt = input("Enter 1 for ecryption and 2 for decrytion\n")
if opt=='1':
    s = input("Enter number as a message\n")
    m = int(s)
    c = pow(m, e, phi)
    print("Cipher text", str(c))
else:
    s = int(input("Enter Chipher text\n"))
    d = pow(s, d, phi)
    print("Plain text", str(d))
