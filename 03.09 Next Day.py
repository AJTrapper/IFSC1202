x = int(input("Enter a Month : "))
y = int(input("Day of Month : "))
# 30 days = 4,6,9,11
# 31 days =1,3,5,7,8,10,12

if x == 4 or x == 6 or x == 9 or x == 11:
    if y != 30:
        print((x) (y+1))
    else:
        print("1")

elif x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10:
    if y != 31:
        print(y+1)
    else:
        print("1")
    
else :
    if y != 28:
        print(y+1)
    else:
        print("1")