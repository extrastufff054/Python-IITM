# Introduction to Strings

# Strings are a sequence of characters
# Strings are immutable
# Strings can be indexed and sliced
# Strings can be concatenated and replicated
# Strings can be tested for membership
# Strings have a length

s = 'coffee'
t = 'bread'
print(s)
print(t)
print(s+t)
print(s,"and " +t)

# Indexing and Slicing
# Indexing starts from 0
# Indexing can be done from the end using negative numbers
# Slicing is done using [start:stop:step]
# start is inclusive and stop is exclusive
# step is optional and default value is 1

s = 'coffee'
print(s[0])        # c
print(s[-1])       # e
print(s[1:4])      # off
print(s[1:6:2])    # ofe   -> step is 2, so it skips every alternate character
print(s[4:1:-1])   # efo   -> step is -1, so it reverses the string
print(s[::-1])     # reverse the string

# Concatenation and Replication
# Concatenation is done using +
# Replication is done using *

s = 'coffee'
t = 'bread'
print(s+t)        # coffeebread
print(s*3)        # coffeecoffeecoffee

s = "0123456789"
a= s[4]
b= s[7]
print(a)
print(b)
print(a+b)
print(int(a+b))
print(int(a)+ int(b)) 