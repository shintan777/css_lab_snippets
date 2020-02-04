"""
Product cipher is a combination of substitution and transformation cipher
"""


def transform(ct, k):
    mat = []
    n = len(ct)
    if(n % k != 0):
        voids = k*(n//k+1) - n
        for something in range(voids):
            ct.append('0')
    for i in range(0, n, k):
        temp = []
        for j in range(k):
            temp.append(ct[i+j])
        mat.append(temp)
    #print('mat', mat)
    ret = []
    for i in range(k):
        for j in range(len(mat)):
            ret.append(mat[j][i])

    #print('ret', ret)
    temp = []
    val = k - 1
    for i in range(len(ret)):
        temp.append(ret[i])
        if(i == 0 or i == len(ret)-1):
            continue
        if(i == val):
            temp.append(' ')
            val += k
    temp = ''.join(temp)
    print(temp)

    return temp  # ''.join(ret)


def rev_transform(ct, k):
    ct = ct.split()
    k_dash = len(ct)
    temp = [[] for i in range(k_dash)]
    ct = ''.join(ct)
    for i in range(k_dash):
        t = i
        for j in range(k):
            try:
                temp[i].append(ct[t])
            except:
                continue
            t += k_dash
    ret = []
    mat = temp
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ret.append(mat[i][j])
    ret = ''.join(ret)
    return ret


opt = input("Enter 1 for ecryption and 2 for decrytion\n")
if opt == '1':
    s = input("Enter text\n")
    s = s.lower()
    s = s.split()
    s = ''.join(s)
    k = int(input("Enter key\n"))
    c = []
    for i in s:
        my_ord = ord(i)
        my_ord += k
        if my_ord > 122:
            my_ord -= 26
        my_chr = chr(my_ord)
        c.append(my_chr)
    c = transform(c, k)
    print("Cipher text", ''.join(c))
else:
    s = input("Enter Cipher text\n")
    s = s.lower()
    k = input("Enter key or leave blank for bruteforce\n")
    if k != '':
        k = int(k)
        s = rev_transform(s, k)
        c = []
        for i in s:
            my_ord = ord(i)
            my_ord -= k
            if my_ord < 97:
                my_ord += 26
            my_chr = chr(my_ord)
            c.append(my_chr)
        print("Plain text", ''.join(c))
    else:
        print("Bruteforcing....")
        for k in range(1, 26):
            output = rev_transform(s, k)
            c = []
            for i in output:
                my_ord = ord(i)
                my_ord -= k
                if my_ord < 97:
                    my_ord += 26
                my_chr = chr(my_ord)
                c.append(my_chr)
            print(" For k = ", k, "Plain text = ", ''.join(c))
# Wrote on python idle ... indent is 1 tab
