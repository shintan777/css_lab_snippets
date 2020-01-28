"""
Product cipher is a combination of substitution and transformation cipher
"""

def transform(ct,k):
    #t=[i for i in ct if i != ' ']
    mat =[]

    for i in range(0,len(ct),k):
        temp = []
        for j in range(k):
            temp.append(ct[i+j])
        mat.append(temp)
    ret =[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
           ret.append(mat[j][i])
        ret.append(' ')
    return ret #''.join(ret)
        
def rev_transform(ct,k):
    ## ct = 'dld ggg lda'
    ct = ct.split()
    k = len(ct[0])
    k_dash = len(ct)//k
    mat = [[] for i in range(k_dash)]    
    ct = ''.join(ct)
    for i in range(k_dash):
        #temp = []
        for j in range(k):     
            mat[j].append(ct[i+j])
        #mat.append(temp)
    ret =[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
           ret.append(mat[i][j])
        ret.append(' ')
    return ret #''.join(ret)
    
opt = input("Enter 1 for ecryption and 2 for decrytion\n")
if opt=='1':
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
    c = transform(c,k=3)
    print("Cipher text", ''.join(c))
else:
    s = input("Enter Cipher text\n")
    s = s.lower()
    k = input("Enter key or leave blank for bruteforce\n")
    s = rev_transform(s,3)
    print(s)
    if k != '':
        k = int(k)
    if k != '': 
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
        for k in range(1,26):
            c = []
            for i in s:
                my_ord = ord(i)
                my_ord -= k
                if my_ord < 97:
                    my_ord += 26
                my_chr = chr(my_ord)
                c.append(my_chr)
            print(" For k = ",k,"Plain text = ", ''.join(c))
### Wrote on python idle ... indent is 1 tab 
