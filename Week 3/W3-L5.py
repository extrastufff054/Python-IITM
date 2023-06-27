# Introduction to for loop in Python
print('''Case 0 : Print hello world using print statement\n
        Case 1 : Print hello world using operator\n 
        Case 2 : Print hello world using for loop\n 
        Case 3 : Print hello world using while loop\n
        Case 4 : Print hello world and hii world alternatively using for loop\n''')
argument = int(input("Choose your case : \n" ))
def switch_case(argument) :
    match(argument) : 
        case 0 :
            print("Print hello world using print statement")
            print("Hello world!!")
            print("Hello world!!")
            print("Hello world!!")
            print("Hello world!!")
            print("Hello world!!")

        case 1 :
            print("Print hello world using operator")
            # What if I want to print 100 times?
            print("Hello world!!") * 100

        case 2 :
            print("Print hello world using for loop")
            # What if I want to print 100 times? (Using for loop)
            for i in range(100):
                print("Hello world!!", i)
        
        case 3 :
            print("Print hello world using while loop")
            # What if I want to print 100 times? (Using while loop)
            i = 0
            while i < 100:
                print("Hello world!!", i)
                i += 1

        case 4 :
            n = int(input("Enter the number of iterations : "))
            for i in range(n) :
                if(i%2 == 0) :
                    print("Hello world!!", i)
                else :
                    print("Hii world!!", i)
switch_case(argument)