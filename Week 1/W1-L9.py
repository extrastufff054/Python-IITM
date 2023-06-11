# Operators and Expressions - 1

a = 10
b = 20
n = a+b
print(n)    # Normal addition of two numbers -> Natural behavior

# -------------------------------------------------------------------

a = 'sudarshan'
b= 'India'
# n = a*b 
# # OR
# n = a/b
print(n)    # This throws an error

# -------------------------------------------------------------------

n = a+b 
print(n)    # Concatenation of strings

# -------------------------------------------------------------------

a = [1,2,3]
b = [7,9,5]
n = a+b
print(n)    # It combines two sets/lists and creates a new list

# -------------------------------------------------------------------

a = 11
b = 15
n = a/b
print(n, type(n))

# -------------------------------------------------------------------

## Operator Precedence

n = 10 + 13 * 2
# My guess is 'n' will be 46
print(n)    # Output = 36 -> Reason : BODMAS or Operator Precedence

