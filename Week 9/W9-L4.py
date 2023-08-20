# Handling very big files


# 1. Read the file line by line : Since it will not get hung

f = open('directory.txt', 'r')

for i in f :
    f.readline()
    print(i, end='')

f.close()
