# Introduction to Import library
import math
# The math module implements many of the IEEE functions that would normally be found in the native platform C libraries for complex mathematical operations using floating point values, including logarithms and trigonometric operations.
print('The log of 10 is : ',math.log(10))
print('Value of sin(45) : ',math.sin(45))
print('cos(45) : ',math.cos(45))
print('sin(90) : ',math.sin(90))
print('sqrt(34)',math.sqrt(34))
print('Factorial of 10 is : ', math.factorial(10))
print('Power (2^3) : ',math.pow(2,3))
print('------------------------------------------------')

import random
# The random module provides access to functions that support many operations. Perhaps the most important thing is that it allows you to generate random numbers.
print(random.random())      # Random float x, 0.0 <= x < 1.0

# Let us simulate a coin toss
print('Coin toss :', random.choice(['heads', 'tails']))

print('By tutor')
a = random.random()
if(a<0.5) :
    print("Heads")
else :
    print("Tails")

print('------------------------------------------------')

# Let us simulate a dice roll (six faced)

print('Dice roll', random.randrange(1,7))    # Random integer from 1 to 6 inclusive

print('------------------------------------------------')

dice1 = (random.randrange(1,7))
dice2 = (random.randrange(1,7))
total = dice1 + dice2

print('Your pair of dice is : ', total)