# Caesar cipher

'''This program considers an input file and encrypts it using Caesar cipher.
By that we mean, we shift the letter by 3 units. For example, a becomes d, b becomes e, and so on.'''

import string
def create_caesar_dictionary() :
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)) :
        d[l[i]] = l[(i-3)%26]
    return d

f = open('encrypted.txt', 'r')
g = open('decrypted.txt', 'w')

d = create_caesar_dictionary()
c = f.read(1)
while(c!='') :
    if c.isalpha() and c.lower() in d:
        if c.isupper() :
            g.write(d[c.lower()].upper())
        else :
            g.write(d[c])
    c = f.read(1)

f.close()
g.close()

f = open('decrypted.txt', 'r')
print(f.read())