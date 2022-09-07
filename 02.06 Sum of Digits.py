a = int(input("Enter a Number :"))
b = a//1000
c = (a%1000)//100
d = (a%100)//10
e = (a%10)//1
f = int(b)+int(c)+int(d)+int(e)
print(f)