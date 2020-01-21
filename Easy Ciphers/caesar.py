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
    print("Cipher text", ''.join(c))
else:
    s = input("Enter Chipher text\n")
    s = s.lower()
    k = input("Enter key or leave blank for bruteforce\n")
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
