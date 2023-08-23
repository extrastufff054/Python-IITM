class Person : 
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def display(self) :
        print(self.name, self.age)

class Student(Person) :
    def __init__(self, name, age, marks) :
        super().__init__(name, age)
        self.marks = marks

    def display(self) :
        super().display()
        print(self.marks)

class Employee(Person) :
    def __init__(self, name, age, salary) :
        super().__init__(name, age)
        self.salary = salary

    def display(self) : # Method Overriding
        print(self.name, self.age, self.salary)

s = Student('Bottle', 20, 239)
s.display()

e = Employee('Earphones', 30, 20000)
e.display()

# To declare private members in a class we add '__' before the variable
'''For eg. 
class Person :
    def __init__(self, name, age) :
    self.name = name 
    self.__age = age #Private member of the class Person
'''

'''Types of Inheritance : 4 types of inheritance 
1) simple inheritance => 1 parent -> child
2) Hierarchial inheritance => parent -> multiple children
3) Multiple Inheritance => Multiple parents -> single child
4) Multilevel Inheritance => Parent class -> Intermediate class -> Child class
5) Hybrid Inheritancen -> Combination of above mentioned inheritance
