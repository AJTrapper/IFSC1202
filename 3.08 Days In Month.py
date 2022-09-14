x = int(input("Enter a Month : "))
# 30 days = 4,6,9,11
# 31 days =1,3,5,7,8,10,12

if x == 4 or x == 6 or x == 9 or x == 11:
    print("30 Days")

elif x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print("31 Days")

else :
    print ("28 Days") 