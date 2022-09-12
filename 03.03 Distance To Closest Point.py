a = int(input("Enter Point A :"))
b = int(input("Enter Point B :"))
c = int(input("Enter Point C :"))
x = abs((a)-(b))
y = abs((a)-(c))
z = abs((b)-(c))
if x < y and x < z:
    print(x)

elif y < x and y < z:
    print(y)

else :
    print (z)