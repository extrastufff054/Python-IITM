# An interesting cipher : More on strings
# Caesar Cipher
alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha[0])
i = 10 
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])

print('------------------------------------------------')

print(alpha[20])
i = 30
print('alpha[i%26] = ',alpha[i%26])
print('alpha[i%26+1] = ',alpha[i%26+1])
print('alpha[i%26+2] = ',alpha[i%26+2])

print('------------------------------------------------')

s = 'sudarshan'
#1. I expect to output : tvebstibo
t = ''
print(alpha.index(s[0]))
print(alpha[(((alpha.index(s[0]))+1)%26)])
t += alpha[(((alpha.index(s[0]))+1)%26)]
print(t)

i = 0
t += alpha[(((alpha.index(s[i]))+1)%26)]
t += alpha[(((alpha.index(s[i+1]))+1)%26)]
t += alpha[(((alpha.index(s[i+2]))+1)%26)]

print('------------------------------------------------')

print("If we want to shift by 2")
alpha = "abcdefghijklmnopqrstuvwxyz"
c = 'chennai'
t = ''
i = 0
k = 1
t += (alpha[(((alpha.index(c[i]))+k)%26)])
t += (alpha[(((alpha.index(c[i+1]))+k)%26)])
t += (alpha[(((alpha.index(c[i+2]))+k)%26)])
t += (alpha[(((alpha.index(c[i+3]))+k)%26)])
t += (alpha[(((alpha.index(c[i+4]))+k)%26)])
t += (alpha[(((alpha.index(c[i+5]))+k)%26)])
t += (alpha[(((alpha.index(c[i+6]))+k)%26)])
print(t)

print('------------------------------------------------')

