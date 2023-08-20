f = open('directory.txt', 'r')
flag = 0

s = '0'
while(s!='') :
    s = f.readline()
    if s !='' :
        n = int(s)
        if (n == 9020214197) :
            print("Found!!")
            flag = 1
            break
if flag == 0 :
    print("Not Found!!")