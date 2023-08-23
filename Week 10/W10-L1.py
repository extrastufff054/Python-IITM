# Introduction to Object Oriented Programming (OOP)

# Classes and Objects

class Student : #class keyword is used to define a class 
    # first letter for class_name is capitalized as a good practice
    roll_no = None
    name = None

s0 = Student() # s0 is an object of class 'Student'
# Student() is called as a constructor
s0.roll_no = 0
s0.name = 'Bhuvanesh'
print(s0.roll_no, s0.name)

s1 = Student()
print(s1.roll_no, s1.name)

s2 = Student()
s2.roll_no = 2
s2.name = 'Harish'
print(s2.roll_no, s2.name)

s50 = Student()
s50.name = 'Anushka'
print(s50.roll_no, s50.name)


