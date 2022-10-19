y = input("Enter Values Seperated by Spaces: ")
x = y.split()
for i in range(1,len(x)):
     x.count(x[i])
print(distinct)