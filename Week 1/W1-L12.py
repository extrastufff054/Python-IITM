# More on Strings

#1. Replication
#2. Indexing
#3. Slicing
#4. Membership
#5. Length
#6. Immutability
#7. Concatenation
#8. Type Conversion
#9. Escape Sequences
#10. String Methods
#11. String Comparison

# Replication
# Replication is done using *

s = 'good'
print(s*3)        # goodgoodgood
print('------------------------------------------------')
# Indexing (Negative string indexing )
# Indexing starts from 0
# Indexing can be done from the end using negative numbers
print("Indexing", "\n------------------------------------------------")
s = 'coffee'
print(s[0])        # c
print(s[-1])       # e
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print('------------------------------------------------')
print("Slicing", "\n------------------------------------------------")
# Slicing
# Slicing is done using [start:stop:step]
# start is inclusive and stop is exclusive
# step is optional and default value is 1

s = 'coffee'
print(s[1:4])      # off
print('------------------------------------------------')
print("Membership", "\n------------------------------------------------")
# Membership
# Strings can be tested for membership using in and not in operators

s = 'coffee'
print('f' in s)    # True
print('x' in s)    # False
print('x' not in s)# True
print('------------------------------------------------')
print("Length", "\n------------------------------------------------")
# Length
# Length of a string can be found using len() function

s = 'coffee'
print(len(s))      # 6
print('------------------------------------------------')
print("Immutability", "\n------------------------------------------------")
# Immutability
# Strings are immutable

s = 'coffee'
# s[0] = 't'         # TypeError: 'str' object does not support item assignment
print('------------------------------------------------')
print("Concatenation", "\n------------------------------------------------")
# Concatenation
# Concatenation is done using +

s = 'coffee'
t = 'bread'
print(s+t)        # coffeebread
print('------------------------------------------------')
print("Type Conversion", "\n------------------------------------------------")
# Type Conversion
# Strings can be converted to int and float using int() and float() functions

s = '123'
print(int(s))     # 123
print(float(s))   # 123.0
print('------------------------------------------------')
print("Escape Sequences", "\n------------------------------------------------")
# Escape Sequences
# Escape sequences are used to insert characters that are illegal in a string

# \n - newline
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote

print('Hello\nWorld')       # Hello
                            # World
print('Hello\tWorld')       # Hello   World
print('Hello\\World')       # Hello\World
print('Hello\'World')       # Hello'World
print('Hello\"World')       # Hello"World
print('------------------------------------------------')
print("String Methods", "\n------------------------------------------------")
# String Methods
# Methods are functions that are associated with an object
# Methods are accessed using the dot operator
# Methods are in the form of object.method()

# capitalize() - capitalize the first character of the string
# count() - count the number of occurrences of a substring
# find() - find the index of the first occurrence of a substring
# index() - find the index of the first occurrence of a substring
# isalnum() - check if all characters in the string are alphanumeric
# isalpha() - check if all characters in the string are alphabetic
# isdigit() - check if all characters in the string are digits
# islower() - check if all characters in the string are lowercase
# isupper() - check if all characters in the string are uppercase
# isspace() - check if all characters in the string are whitespace
# lower() - convert all characters in the string to lowercase
# upper() - convert all characters in the string to uppercase
# replace() - replace a substring with another substring
# split() - split the string into substrings based on the delimiter
# strip() - remove leading and trailing whitespace
# join() - join a list of strings into one string

# capitalize() - capitalize the first character of the string

s = 'coffee'
print(s.capitalize())       # Coffee

# count() - count the number of occurrences of a substring

s = 'coffee'
print(s.count('f'))         # 1

# find() - find the index of the first occurrence of a substring

s = 'coffee'
print(s.find('f'))          # 1

# index() - find the index of the first occurrence of a substring

s = 'coffee'
print(s.index('f'))         # 1

# isalnum() - check if all characters in the string are alphanumeric

s = 'coffee'
print(s.isalnum())          # True

# isalpha() - check if all characters in the string are alphabetic

s = 'coffee'
print(s.isalpha())          # True

# isdigit() - check if all characters in the string are digits

s = '123'
print(s.isdigit())          # True

# islower() - check if all characters in the string are lowercase

s = 'coffee'
print(s.islower())          # True

# isupper() - check if all characters in the string are uppercase

s = 'COFFEE'
print(s.isupper())          # True

# isspace() - check if all characters in the string are whitespace

s = ' '
print(s.isspace())          # True

# lower() - convert all characters in the string to lowercase

s = 'COFFEE'
print(s.lower())            # coffee

# upper() - convert all characters in the string to uppercase

s = 'coffee'
print(s.upper())            # COFFEE

# replace() - replace a substring with another substring

s = 'coffee'
print(s.replace('f','t'))   # cottee

# split() - split the string into substrings based on the delimiter

s = 'coffee'
print(s.split('f'))         # ['cof', '', 'ee']

# strip() - remove leading and trailing whitespace

s = ' coffee '
print(s.strip())            # coffee

# join() - join a list of strings into one string

s = ['coffee','bread']
print(' '.join(s))          # coffee bread
print('------------------------------------------------')
print("String Comparison", "\n------------------------------------------------")
# String Comparison
# Strings can be compared using ==, !=, <, >, <=, >= operators
# Comparison is done based on the ASCII value of the characters

x = 'India'
print(x == 'India')         # True
print(x == 'india')         # False

print('apple' > 'one')    # True
print('four' < 'ten')    # False

print('ab' < 'az')  # True
print('abcdef' < 'abcde')   # False
