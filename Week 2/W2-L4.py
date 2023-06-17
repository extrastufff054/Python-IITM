# Escape characters and types of quotes

#1. Escape characters
#print('It's a beautiful day')  # Error
print('It\'s a beautiful day') # '\' is used in order to print apostrophe 's' as an escape character
print("We are form \"IIT\"Madras")
print("My name is Sarang, I an from Pune")
print("My name is Sarang. \tI am from Pune")
print("My name is Sarang.\n I am from Pune")


# Use of quotes supported by Python
x= 'this is a string'
y = "This is also a string"
z = 'first line \n second line \n third line'
print(x,y,z)
z= '''first line
second line 
third line 
forth line
fifth line'''
print(z)

'''This is a multi-line comment
Line1
Line 2 
Line 3'''