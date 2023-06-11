# Operators and Expressions - 2

#1. Arithmetic Operators (+, -, *, /, %, //, **)

print('Addition', 2+3)                      # Gives the sum
print('Subtraction', 2-3)                   # Gives the difference
print('Multiplication', 2*3)                # Gives the product
print('Division', 2/3)                      # Gives the quotient

print('Modulus', 2%3)                       # Gives the remainder
print('Floor Division', 2//3)               # Gives the quotient
print('Exponent', 2**3)                     # 2 to the power 3
print('---------------------------')

#2. Relational Operators (>, <, >=, <=, ==, !=)

print('Greater than', 2>3)                  # Checks if 2 is greater than 3
print('Less than', 2<3)                     # Checks if 2 is less than 3
print('Greater than or equal to', 2>=3)     # Checks if 2 is greater than or equal to 3
print('Less than or equal to', 2<=3)        # Checks if 2 is less than or equal to 3
print('Equal to', 2==3)                     # Checks if 2 is equal to 3
print('Not equal to', 2!=3)                 # Checks if 2 is not equal to 3
print('---------------------------')

#3. Logical Operators (and, or, not)

# Logical AND - Returns True if both the operands are True
print('Logical AND', True and True)        
print('Logical AND', True and False)        
print('Logical AND', False and True)
print('Logical AND', False and False)

# Logical OR - Returns True if any one of the operands is True
print('Logical OR', True or True)
print('Logical OR', True or False)
print('Logical OR', False or True)
print('Logical OR', False or False)

# Logical NOT - Returns True if the operand is False
print('Logical NOT', not True)
print('Logical NOT', not False)
print('---------------------------')

#4. Bitwise Operators (&, |, ^, ~, <<, >>)

# Bitwise AND - Returns 1 if both the bits are 1
print('Bitwise AND', 10 & 4)                # 10 -> 1010, 4 -> 0100, 1010 & 0100 -> 0000 -> 0

# Bitwise OR - Returns 1 if any one of the bits is 1
print('Bitwise OR', 10 | 4)                 # 10 -> 1010, 4 -> 0100, 1010 | 0100 -> 1110 -> 14

# Bitwise XOR - Returns 1 if the bits are different
print('Bitwise XOR', 10 ^ 4)                # 10 -> 1010, 4 -> 0100, 1010 ^ 0100 -> 1110 -> 14

# Bitwise NOT - Returns 1 if the bit is 0
print('Bitwise NOT', ~10)                   # 10 -> 1010, ~10 -> 0101 -> 5

# Bitwise Left Shift - Shifts the bits to the left by the specified number of places
print('Bitwise Left Shift', 10 << 2)        # 10 -> 1010, 1010 << 2 -> 101000 -> 40

# Bitwise Right Shift - Shifts the bits to the right by the specified number of places
print('Bitwise Right Shift', 10 >> 2)       # 10 -> 1010, 1010 >> 2 -> 10 -> 2

#5. Assignment Operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, ~=, <<=, >>=)

a = 10
print('Assignment Operator', a)             # a = 10

a += 10
print('Assignment Operator', a)             # a = a + 10 -> 20

a -= 10
print('Assignment Operator', a)             # a = a - 10 -> 10

a *= 10
print('Assignment Operator', a)             # a = a * 10 -> 100

a /= 10
print('Assignment Operator', a)             # a = a / 10 -> 10.0

a %= 10
print('Assignment Operator', a)             # a = a % 10 -> 0.0

a //= 10
print('Assignment Operator', a)             # a = a // 10 -> 0.0

a **= 10
print('Assignment Operator', a)             # a = a ** 10 -> 0.0    

a &= 10
print('Assignment Operator', a)             # a = a & 10 -> 0   

a |= 10
print('Assignment Operator', a)             # a = a | 10 -> 10

a ^= 10
print('Assignment Operator', a)             # a = a ^ 10 -> 0

a = ~10
print('Assignment Operator', a)             # a = a ~ 10 -> -11

a <<= 10
print('Assignment Operator', a)             # a = a << 10 -> -11264 

a >>= 10    
print('Assignment Operator', a)             # a = a >> 10 -> -12

