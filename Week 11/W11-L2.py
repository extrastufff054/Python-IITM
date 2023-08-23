# Functional Programming(Part 1)

fruits = ["mango","apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

basket = iter(fruits)   #Any iterable entity can be converted into an iterator

print(next(basket))

# ------------------------------------------------------------------------------------

# Program to create a generator

def square(limit) : # Generator
    x = 0
    while x<limit :
        yield x * x
        yield x * x * x
        x+=1

a = square(5)  # a is an iterator
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))

