x = int(input("First number : "))
y = int(input("Second number : "))
z = int(input("Third Number : "))
if x<y and x<z:
    if y<z:
        print(x,y,z)
    else:
        print(x,z,y)    

elif y<x and y<z:
    if x<z:
        print(y,x,z)
    else:
        print(y,z,x)   

else :
    if x<y:
        print(z,x,y)
    else:
        print(z,y,x)   