x = int(input("Enter Number (zero to quit): "))
maximumvalue = x
maximumindex = 1
currentindex = 0
while x != 0:
    currentindex = currentindex + 1
    if x > maximumvalue:
        maximumvalue = x
        maximumindex = currentindex
    x = int(input("Enter Number (zero to quit): "))
print("Maximum:  {}".format(maximumvalue))
print("Index of Maximum:  {}".format(maximumindex))