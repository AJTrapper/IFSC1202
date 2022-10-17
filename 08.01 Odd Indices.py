y = input("Enter Values Seperated by Spaces: ")
x = y.split()
for i in range(len(x)):
    if i % 2==1:
        print (x[i])