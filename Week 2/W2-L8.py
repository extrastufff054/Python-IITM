# Tutorial on if, else and elif conditions

# Problem 1 : Find whether the given number is even or odd
print('Problem 1 : Find whether the given number is even or odd')

x = int(input("Enter the number :"))

if(x%2 == 0) :
    print("The number is even")

else : 
    print("The number is odd")

print('------------------------------------------------')

# Problem 2 : Find whether the given number ends with 0 or 5 or any other number

print('Problem 2 : Find whether the given number ends with 0 or 5 or any other number')
y = int(input("Enter the number :"))

if(y%5==0) :
    print("The number ends with 5")
elif(y%10==0) :
    print("The number ends with 0")
else :
    print("The number ends with some other number")

print('------------------------------------------------')

print('Solution by tutor')

num = int(input("Enter the number :"))
if(num % 5==0) :
    if(num % 10==0) :
        print("The number ends with 0")
    else :
        print("The number ends with 5")

else : print('Other')

print('------------------------------------------------')

# Problem 3 : Find the grade of student based on the given marks from 0 to 100

print('Problem 3 : Find the grade of student based on the given marks from 0 to 100')

marks = int(input("Enter the marks :"))
if(marks <= 100 or marks >= 0) :
    if(marks >=90) :
        print('A')

    elif(marks >=80) :
        print('B')

    elif(marks >=70):
        print('C')

    elif(marks >=60):
        print('D')

    else : print('E')
else : print('Invalid input')

print('------------------------------------------------')

print('Solution by tutor')
marks = int(input("Enter the marks :"))
if(marks <= 100 or marks >= 0) :
    if(marks >= 90) :
        print('A')
    if(marks>= 80 and marks <90) :
        print('B')
    if(marks>= 70 and marks <80) :
        print('C')
    if(marks>= 60 and marks <70) :
        print('D')
    if(marks<60) :  
        print('E')
else : print('Invalid input')

print('------------------------------------------------')

# Problem 4 : Convert the given flowchart into a Python code
print('Travel from city A to city B')
time = int(input("Enter the time :"))
longer = int(input("Define longer :"))
if(time >= longer) :
    price = int(input("Enter the price :"))
    higher = int(input("Define higher :"))
    if(price >= higher) :
        print("Travel by train")
    else :
        print("Travel by Coach")
              
else : 
    price = int(input("Enter the price :"))
    higher = int(input("Define higher :"))
    if(price >=higher) : 
        print("Travel by Daytime Flight")
    else : 
        print('Red eye flight')

print('Arrive city B')

print('------------------------------------------------')