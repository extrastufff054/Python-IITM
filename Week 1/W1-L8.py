# Data types - 2

## Data type = Boolean - True or False
b1 = True
b2 = False
print(type(b1), type(b2))

## Data Conversion (Type Casting)

# int() - converts to integer
a = int(5.7)     # converts float to int
b=int('10')     # converts string to int

print(a, type(a))
print(b, type(b))
print('---------------------------')

# ------------------------------------------------------------

# float() - converts to float
c=float(5)      # converts int to float
d=float('10.5') # converts string to float

print(c, type(c))
print(d, type(d))
print('---------------------------')

# ------------------------------------------------------------

# str() - converts to string
e=str(5)        # converts int to string
f=str(19.4)     #converts float to string

print(e, type(e))
print(f, type(f))
print('---------------------------')

# bool() - converts to boolean
g=bool (10)      # converts int to boolean
h = bool(0)      # converts int to boolean
i = bool(-10)    # converts int to boolean

print(g, type(g))
print(h, type(h))
print(i , type(i))
print('---------------------------')

j= bool(10.5)    # converts float to boolean
k = bool(0.0)    # converts float to boolean
l = bool(-10.4)  # converts float to boolean

print(j, type(j))
print(k, type(k))
print(l, type(l))
print('---------------------------')

m= bool('India')    # converts string to boolean
n = bool((''))      # converts string to boolean    -> An boolean conversion of empty string is false
o = bool('10')      # converts string to boolean
p = bool('0')        # converts string to boolean
q = bool('False')    # converts string to boolean

print(m, type(m))
print(n, type(n))
print(o, type(o))
print(p, type(p))
print(q, type(q))
print('---------------------------')