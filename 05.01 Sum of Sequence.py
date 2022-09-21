x = int(input("Enter Number (zero to quit): "))
sum = 0
while x != 0:
    sum = sum + x
    x = int(input("Enter Number (zero to quit): "))
print("Sum:  {}".format(sum))
