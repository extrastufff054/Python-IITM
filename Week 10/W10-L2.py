# Attributes and Methods

''' init : is a special method that serves as the constructor for a class. It is automatically called when an object of the class is created. The '__init__' method is used to initilize the attributes or properties of an object with default or provided values
'''

'''
self : is a conventional name for the first parameter of a method in a class. It refers to the instance of the class that the method is being called on.
When you define methods withing a class, you tpecally use 'self' as the first parameter in those methdods to reference the instance that the method is operating on.
'''
class Student :
    count = 0 #Local variable scope : class definition

    def __init__(self, roll_no, name, total) :
        self.roll_no = roll_no #self.name and self.roll_no are object variables i.e. attributes 
        self.name = name # where as roll_no and name are function variables with scope limited to the function definition
        self.total = total

    def display(self) :
        print(self.roll_no, self.name)
    
    def result(self) :
        if self.total > 120 :
            print("Pass")
        else : 
            print("Fail")

s0 = Student(0,'Bhuvanesh',100)
Student.count += 1
s0.display()

s1 = Student(1,'Harish',150)
Student.count +=1
s1.display()

# Variables inside __init__() belong to object and variables inside class only belong to the class(class attribute)

print(Student.count)
print('--'*20)
s0.display()
s0.result()
s1.display()
s1.result()

