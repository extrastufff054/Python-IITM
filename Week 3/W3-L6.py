# For loop to add the first n numbers

argument = int(input("Choose your case: "))

def switch_case (argument) :
    match argument :
        case 0 :
            # 1. Find the sum of 10 numbers
                r = 10
                sum = 0
                i = 1
                for i in range(r) : 
                    print("Input",i," :", end = " ")
                    n = int(input())
                for i in range(r) :
                     sum += i
                print("Output :", sum)

        case 1 :
            # 2. Find the sum of first 12 numbers
                r = 12
                sum = 0
                i = 1
                for i in range(r) :
                        sum += i
                print("Output :", sum)
        
        case 2 :
            # 3. Find the sum of first n numbers
                r = int(input("Enter the range :"))
                sum = 0
                i = 1
                for i in range(r) :
                      sum += i
                print("Output :", sum)

        case 3 :
            # 4. Find the sum of first n numbers (Optimized solution)
                r = int(input("Enter the range :"))
                sum = 0
                sum = (r * (r + 1)) / 2
                print("Output :", sum)
            
        case 4 : 
            # 5. Find the sum of first n even and odd numbers
                r = int(input("Enter the range :"))
                sumEven = 0
                sumOdd = 0
                i = 1
                for i in range(r) :
                    if i % 2 == 0 :
                          sumEven += i
                    else :
                        sumOdd += i
                print("Sum of n Even numbers :", sumEven,"Sum of n Odd numbers", sumOdd)



switch_case(argument)