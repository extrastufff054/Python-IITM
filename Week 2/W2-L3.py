#1. Keywords and naming rules :
#   1.1. Keywords are the reserved words in Python.
#   1.2. We cannot use a keyword as a variable name, function name or any other identifier.
#   1.3. Keywords are case sensitive.
#   1.4. There are 33 keywords in Python 3.7. This number can vary slightly over the course of time.
#   1.5. All the keywords except True, False and None are in lowercase and they must be written as it is.
#   1.6. The list of all the keywords are given below.
#2. Identifiers :
#   2.1. An identifier is a name given to entities like class, functions, variables, etc. in Python.
#   2.2. It helps to differentiate one entity from another.
#   2.3. Rules for writing identifiers :
#       2.3.1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
#       2.3.2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.

# For example : 
#1. for =5 
#   print (for)

#2. and = 10
#   print(and)

a1 = 10
A_b = 20
print(a1, A_b)

# Rules for declaring variables :
#   1.1. Variable names should always start with either an alphabet or an underscore
#   1.2. Variable names are case-sensitive
#   1.3. Multiple assignment : 
x, y, z = 1, 2, 3
print(x,y,z)    # Output : 1 2 3
x = y = z = 10  # Output : 10 10 10

x, y = y, z
print(x, y)

# Removing/Deleting a variable
abc = 10
print(abc)      # Output : 10
del abc
print(abc)      # Output : Error

# Shorthand Operators :
count = 0
count = count + 1
count = count + 1
count = count + 1
count = count + 1
print(count)
count += 1  # += Is a shorthand operator
count += 1
count += 1
count += 1
print(count)
# It is possible to use such shorthand operators with other arithmetic operators 
count2 = 100
count2 -= 20

count3 = 10
count3 *= 2

# 'in' operator
print('alpha' in 'A variable name can only contain alpha-numeric characters and underscores')
print('alpha' in ' A variable name must start with a letter or the underscore character')

# Chaining Opertors
x=5
print(1<x<10)
print(10<X<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x>4)

