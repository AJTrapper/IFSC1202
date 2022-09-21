x = int(input("Enter NUmber N :"))
remainder = 0
for i in range (1,x):
    print( x%i ) 
    if (x%i)>0:
      remainder=remainder + 1  
    else:
        print()
print("remainder {}".format(remainder))  
 

if remainder == (x-2):
    print("Prime")
else:
    print("Composite")
print("space         Space")
print("remainder {}".format(remainder))