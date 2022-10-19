y = input("Enter Values Seperated by Spaces: ")
x = y.split()
for i in range(1,len(x)):
    if x.count(x[i])<x.count(x[i-1]):
        distinctnumber = x[i]
print(distinctnumber)