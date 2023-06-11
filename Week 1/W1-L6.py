# Variables and Literals
print("Type your name :")
name=str(input())
print("Type your location : ")
place = str(input())
print("Type your age : ")
age = int(input())

print("Hello", name, "you are", age, "years old and you are from", place, "!!\n")

## ----------------------------------------------------------------------------------------------------
# Can we merge print and input command together?
# print("Type your name :")
# name=str(input())
name=str(input("Type your name :"))
place=str(input("Type your location : "))
age = int(input("Enter your age"))
print("Hello", name, "you are", age, "years old and you are from", place, "!!")

# ------------------------------------------------------------------------------------------------------
name="Sudarshan"
name="Omkar"
name="Sudarshan"
age=40
age=30      # Age and name are known as variables, where as "Sudarshan" and 30 are known as literals
# A variable can store different literal values at different times and they can be modified as per the requirement
age=age+1   # Can be modified
# But, 30=30+1 will throw an error

# Literals can be used only on the right side of the equals to sign
# Whereas, variables can be used on both sides of the equals to sign
# ------------------------------------------------------------------------------------------------------

r=int(input("Enter the radius of the circle :"))
area = 3.14*r*r
print("Area of the circle with radius", r, "is ", area)

# In this above example, r is a variable and 3.14 is a literal, since value of pi=3.14 will never change irrespective of the value of r or area, but r i.e radius can change

# ------------------------------------------------------------------------------------------------------