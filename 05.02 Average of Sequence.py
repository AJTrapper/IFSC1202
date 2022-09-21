x = int(input("Enter Number (zero to quit): "))
sum = 0
cardcount = 0
while x != 0:
    sum = sum + x
    cardcount = cardcount +1
    x = int(input("Enter Number (zero to quit): "))
print("Average:  {}".format(sum/cardcount))
