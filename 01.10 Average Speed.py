a = int(input("Enter Length of Race in Kilometers: "))
b = int(input("Enter Minutes: "))
c = int(input("Enter Seconds: "))
d = int(a)*0.625
e = (int(b)*60) + int(c)
f = (int(d)/int(e))*3600
print(f)