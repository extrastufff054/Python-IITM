# While to compute factorial

print("Enter a number :")
n = int(input())

# What is a factorial !?
# n= 5 then factorial = 5*4*3*2*1

# For n=5
# answer = 1
# answer *= 2
# answer *= 3
# answer *= 4
# answer *= 5
# print(answer)

answer = 1
i = 1
while (i<=n) :
    answer *= i
    i += 1

print("Factorial of",n, "is :", answer)