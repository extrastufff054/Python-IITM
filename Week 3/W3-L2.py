# Introduction to While loop in Python

# While loop is used to execute a block of code multiple times
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1

#1. Quiz program
print("When did India get its independence (year) ?!")
year = int(input())

if(year == 1947) :
    print("Hip hip hooray!! You are correct :)")
else :
    print("Oops!! You are wrong :(")
    print("Come on don't you even know that?")
    print("That's okay, I will give you another chance")
    print("When did India get its independence (year) ?!")
    year = int(input())
    if(year == 1947) :
        print("Hip hip hooray!! You are correct :)")
    else :
        print("Failed in your second attempt too!!? Assfuck!! grrr....")

print('-----------------------------------------------------------------------------------')

#I would like to write a piece of code, which lets the user attempt as many times as he wants.
# The code will end, only when it gets the right answer.

print("When did India get its independence (year) !?")
attempt = 1
while(year != 1947) :
    print("You got this wrong. Try once again!!")
    print("Attempt", attempt)
    attempt += 1
    year = int(input())

print("Woowwwww... you got it right!!")

# While syntax : 
#   while <condition> :
#       your code

print('-------------------------------------------------------------------------------------')