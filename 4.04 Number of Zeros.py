x = int(input("Enter Number N: "))
zerocount = 0
for i in range (x):
    val = int(input("Enter Number: "))
    if val == 0:
       zerocount = zerocount +1
print("Number of Zeros: {}".format(zerocount))