x = int(input("Number of Cards: "))
fulldeck = 0
for i in range (1,x+1):
    fulldeck = fulldeck + i

partialdeck = 0
for i in range(1,x):
    val = int(input("Enter Card: "))
    partialdeck = partialdeck + val

print("Missing Card: {}".format(fulldeck-partialdeck))
