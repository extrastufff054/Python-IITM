# Tutorial on While loop in Python

argument = int(input("Choose your case: "))

def switch_case(argument):
    match argument:
        case 0:
            # 1. Find the factorial of a given number
                # Test case : 5, 2, 0, -7
                # Output : 120, 2, 1, Invalid input
            num = int(input("Enter a number: "))
            fact = 1
            if num < 0:
                print("Invalid input")
                exit()
            else:
                while num > 0:
                    fact *= num
                    num -= 1
                print("Factorial of the given number is:", fact)
                print('-------------------------------------------------------------------------------------')

        case 1:
            # 2. Find the number of digits in the given number
                # Test case : 1234, 123456789, 8, 0, -4
                # Output : 4, 9, 1, 1, 1
            num = abs(int(input("Enter a number: ")))
            digits = 1
            while num > 9:
                num //= 10      # num = num // 10  (floor division)
                digits += 1
            print("Number of digits in the given number is:", digits)
            print('-------------------------------------------------------------------------------------')

        case 2:
            # 3. Reverse the digits in the given number
                # Test case : 1234, 123456789, 9, 0, -1234
                # Output : 4321, 987654321, 9, 0, -4321
                num = int(input("Enter the number : "))
                absNum = abs(num)
                if(num >= 0):
                    rev = num % 10
                    num //= 10
                    while (num > 0) :
                        r = num % 10
                        num //= 10
                        rev = rev * 10 + r
                else:
                    rev = absNum % 10
                    absNum //= 10
                    while (absNum > 0) :
                        r = absNum % 10
                        absNum //= 10
                        rev = rev * 10 + r
                    print(rev - 2 * rev)
        case 3 :
            # 4. Reverse the digits in the given number (Optimized solution)
                # Test case : 1234, 123456789, 9, 0, -1234
                # Output : 4321, 987654321, 9, 0, -4321
                num = int(input("Enter the number : "))
                absNum = abs(num)
                rev = absNum % 10
                while (absNum > 9) :
                    r = absNum % 10
                    absNum //= 10
                    rev = rev * 10 + r
                    if (num >= 0) :
                         print(rev)

                    else :
                        print(rev - 2 * rev)

        case 4: 
              # 5. Find whether the entered number is a palindrome or not
                # Test case : 12321, 1221, 1234, 123421, 9, -1221
                # Output : Palindrome, Palindrome, Not a palindrome, Not a palindrome, Palindrome, Palindrome
                num = int(input("Enter the number :"))
                absNum = abs(num)
                rev = absNum % 10
                absNum //= 10
                while(absNum > 0):
                    r = absNum % 10
                    absNum //= 10
                    rev = rev * 10 + r

                    if(num < 0) :
                         rev = rev - 2 * rev
                    if(num == rev) :
                         print("Palindrome")
                    else :
                        print("Not a palindrome")

        
# Call the function with the input argument
switch_case(argument)
