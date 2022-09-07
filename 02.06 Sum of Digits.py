a = int(input("Enter a Number :"))
b = a//1000
#finds 1000's 

c = (a%1000)//100
#finds 100's digit

d = (a%100)//10
#finds 10's digit

e = (a%10)//1
#finds 1's digit

f = int(b)+int(c)+int(d)+int(e)
print(f)