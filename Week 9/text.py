import random
f = open('directory.txt', 'w')
for i in range(10000) :
    random_number = random.randint(1000000000, 9999999999)
    f.write(str(random_number) + '\n')
f.close()

# f = open('directory.txt', 'r')
# print(f.read())
# f.close()
