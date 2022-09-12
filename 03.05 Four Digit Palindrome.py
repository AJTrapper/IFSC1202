a = int(input("Enter Number :"))
b = a//1000
c = (a%1000)//100
d = (a%100)//10
e = a%10
x = b
y = c
z = d
w = e

if x == w and y == z:
    print("Yes")

else :
    print ("No")