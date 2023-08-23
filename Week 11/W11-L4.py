# Functional Programming (Part 3)

#1. Lambda Function : A lambda function is a small, anonymous function that can have any number of arguments, but can only have one expression.

def add(x,y) :
    return x+y
def sub(x,y) :
    return x-y

def mul(x,y) :
    return x*y

def div(x,y) :
    return x/y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

# Using lambda function

add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda xmy : x/y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

# Enumerate 
fruits = ["mango","apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
size = [5,5,6,6,9,10,5,4]

for fruit in fruits :
    print(fruit)

for i in range(len(fruits)) : #Enumerated iteration
    print(i,fruits[i])

for fruit in enumerate(fruits) : #Enumerated iteration
    print(fruit)

print(zip(fruits,size)) #zip object 
print(list(zip(fruits,size))) #List of tuples
print(dict(zip(fruits,size))) #Dictionary of tuples

# -------------------------------------------------------------------------------------
import math

a = [10,20,30,40,50,60]
b = [5,10,15,20,25,30]
m = [25,-16,9,81,-100]

# We want to do c = a - b
def sub(x,y) :
    return x-y

def incr(x) :
    return x+1

def square_root(m) :
    return math.sqrt(m)

c = map(sub,a,b) #Map function
c = map(incr,a)
c = map(square_root,filter(is_positive,m) #filter function
print(list(c))
