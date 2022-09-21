x = int(input("Enter Number (zero to quit): "))
consecutive = x
count = 1
while x != 0:
    if x != consecutive:
        consecutive = x
        count = 1
    elif x == consecutive:
        consecutive = x
        count = count +1
    x = int(input("Enter Number (zero to quit): "))
    
    
    
    
print("{} repeated {} times".format((consecutive),(count)))