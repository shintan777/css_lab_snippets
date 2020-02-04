"""
Basic rsa algorithm with encryption and decryption
"""
from math import gcd


def coprime(x):
    for i in range(2,x):
        if(gcd(x,i)==1):
            return i
    raise ValueError("Cannot find coprime of {}".format(x))


opt = input("Enter 1 for ecryption and 2 for decrytion\n")
if opt=='1':
    s = input("Enter text\n")
    s = s.lower()
    s = s.split()
    s = ''.join(s)
    k = int(input("Enter key\n"))
    c = []
    """
    ## code here
    """
    print("Cipher text", ''.join(c))
else:
    s = input("Enter Chipher text\n")
    s = s.lower()
    k = input("Enter key or leave blank for bruteforce\n")
    if k != '':
        k = int(k)
    if k != '': 
        c = []
        ##code here
        print("Plain text", ''.join(c))
    else:
        print("Bruteforcing....")
        for k in range(1,26):
            c = []
            ##code here    
        print(" For k = ",k,"Plain text = ", ''.join(c))
### Wrote on python idle ... indent is 1 tab 
