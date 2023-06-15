# Dynamic Typing - We are trying to illustrate what we call dynamic typing in Python.
# It allows to type cast a variable to any type of data.
a = 10 
print(type(a))

a = 'India'
print(type(a))

print('---------------------------------------')

n=10
print(type(n))  # Output: <class 'int'>
print(n)        # Output: 10
n=n/2           
print(type(n))  # Output: <class 'float'>
print(n)        # Output: 5.0

print('---------------------------------------')

# In python, if the division operator is used, the result is always a float. Irrespective of the data type of the operands.
# In the above example, the data type of n is int. But when we divide it by 2, the result is a float.
# This is called dynamic typing. The data type of the variable is decided at runtime.

