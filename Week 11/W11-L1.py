# Exception Handling

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b : "))
try :
    f = open('abc.txt','r')
    c = a/b
    print(d) 
except ZeroDivisionError :
    print("Invalid input, divisor cannot be zero")
    # or we could simply write 'pass'

except NameError :
    print("Varible not defined")

except FileNotFoundError :
    print("Invalid file name!! Please check again")

except :    # If error is not defined or known
    print("Something went wrong!!") 

finally :
    f.close()
    print("Hello from finally block!!")

# What if an exception occurs in finally block

# --------------------------------------------------------------------------

# User defined exceptions

a = int(input())
if a<18 :
    raise Exception("You are underage, cannot vote")

