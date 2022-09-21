secondmax = int(input("Enter Number (zero to quit): "))
firstmax = int(input("Enter Number (zero to quit): "))
x = int(input("Enter Number (zero to quit): "))
while x != 0:
    if x > firstmax:
        firstmax, secondmax = x, firstmax
    elif x > secondmax:
        secondmax = x

    x = int(input("Enter Number (zero to quit): "))
print("First Maximum:  {}".format(firstmax))
print("Second Maximum: {}".format(secondmax))