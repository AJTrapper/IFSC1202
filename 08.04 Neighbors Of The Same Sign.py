y = input("Enter Values Seperated by Spaces: ")
x = y.split()
for i in range(len(x)):
    if int(x[i])<0:
        print("{} Negative".format(x[i]))
    else:
        print("{} positive".format(x[i]))