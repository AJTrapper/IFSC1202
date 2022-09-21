x = int(input("Enter Number (zero to quit): "))
maximum = x
while x != 0:
    if x > maximum:
        maximum = x
    x = int(input("Enter Number (zero to quit): "))
print("Maximum:  {}".format(maximum))
