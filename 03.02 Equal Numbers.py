x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))

if x == y and x == z:
    print(3)

elif y == x or y == z or z == x:
    print(2)

else :
    print (0)