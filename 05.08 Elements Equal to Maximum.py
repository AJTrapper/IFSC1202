x = int(input("Enter Number (zero to quit): "))
maximum = x
maximumcount = 1
while x != 0:
    if x > maximum:
        maximum = x
        maximumcount = 1
    elif x == maximum:
        maximumcount = maximumcount + 1
    x = int(input("Enter Number (zero to quit): "))
print("Maximum:  {}".format(maximum))
print("Number of Occurrences:  {}".format(maximumcount))