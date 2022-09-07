a = int(input("Enter First Two Digit Number: "))
b = int(input("Enter Second Two Digit Number: "))
c = (a//10)*1000
#1000's
d = (a%10)*10
#10's
e = (b//10)*100
#100's
f = b%10
#1's
g = c+d+e+f
print("Merge Number : {}".format(g))