# Reading and Writing to a File


# Creating and writing to a file 

# f = open("test.txt", "w")         #Creating a file and # w = write, r = read, a = append, r+ = read and write
# # f.write("Hello world!!")
# # f.write("This is a new text file")
# f.close()

x = open("test.txt", "r")
print(x.read())
s = x.read()
print(s)
type(s)
x.close()

print('----------------------------------------------------------------------------------------------------------------------------------------')
# Reading a file line by line

f = open('test1.txt', 'w')
f.write('Hello world!!')
f.write('\n This is the second line')
f.write('\n This is the third line')
f.close()

f = open('test1.txt', 'r')
print(f.read())