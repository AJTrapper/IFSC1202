y = input("Enter Values Seperated by Spaces: ")
x = y.split()
for i in range(1,len(x)):
    if int(x[i])>int(x[i-1]):
        print (x[i])