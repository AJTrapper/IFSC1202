previousvalue = int(input("Enter Number (zero to quit): "))
previousmaxcount = 0
while previousvalue != 0:
    currentvalue = int(input("Enter Number (zero to quit): "))
    if currentvalue > previousvalue:
        previousmaxcount = previousmaxcount + 1
    previousvalue = currentvalue
print("Number of Values Greater than the Previous :{}".format(previousmaxcount))