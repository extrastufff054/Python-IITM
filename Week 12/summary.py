# Formatted printing
name = input("Enter some random a$$ name")
print(f'Hi, {name}!')
print('Hi, {}!'.format(name))

# Escape characters

#1. Newline : \n

#2. Tab : \t

#3. Backslash : \\
print("Path : C:\\Documents\\File.txt")

#4. Single Quote or Double Quotes
print('She said, "Hello!"')

#5. Unicode Escape : \u
print("\u03B1")

#6. Raw Strings 
print(r'C:\Users\Username\Documents')

# Range function in for loop : 
# Syntax -> range(start, end, step)

for i in range(1,6,2) :
    print(i)

i = input("Enter any text :")
if i.isalpha() :
    print("It's a string")
else :
    print("It's not a string")