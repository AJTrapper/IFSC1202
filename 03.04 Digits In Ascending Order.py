a = int(input("Enter Number :"))
b = a//100
c = (a%100)//10
d = a%10
x = b
y = c
z = d
if x < y and y < z:
    print("Yes")

else :
    print ("No")