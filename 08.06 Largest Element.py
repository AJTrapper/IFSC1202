y = input("Enter Values Seperated by Spaces: ")
x = y.split()
maxvalue = x
maxindex = 0
for i in range(1,len(x)):
    if int(x[i])>int(x[i-1]):
        maxvalue  = x[i]
        maxindex = i+1
print("Largest Value: {}".format(maxvalue))
print("Index of Largest Value: {}".format(maxindex))
