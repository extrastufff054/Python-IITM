# Functional programming (Part 2)

a = 40
b = 20

'''
if a<b :
    small = a
else :
    small = b
'''
small = a if a<b else b
print(small)

# -------------------------------------------------

a = 5
while a>0 :
    print(a)
    a-= 1

# This can be written in a single line

a = 5
while a>0 : print(a); a-=1
#This reduces number of lines

# -------------------------------------------------

#List comprehension

fruits = ["mango","apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]\
'''
newList = []
for fruit in fruits :
    if 'n' in fruit :
        newList.append(fruit.capitalie())
'''

newList = [fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newList)
