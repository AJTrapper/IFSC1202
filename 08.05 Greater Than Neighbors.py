y = input("Enter Values Seperated by Spaces: ")
x = y.split()
z = 0
for i in range(1,len(x)):
    if int(x[i])>int(x[i-1]):
        z=z+1
print(z)