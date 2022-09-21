x = int(input("Enter Number (zero to quit): "))
evencount = 0
while x != 0:
    if x%2==0:
        evencount = evencount +1
    x = int(input("Enter Number (zero to quit): "))
print("Number of Even Values :{}".format(evencount))