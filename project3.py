def isEven(x):
    if x%2==0:
        return True
    else:
        return False
def isOdd():
    if x%2==0:
        return False
    else:
        return True

def isPrime():
    for i in range (2,(x // 2)  + 1):
        if (x%i)==0:
            return False
    else:
        return True

originalnumbers = open("06.06 Numbers.txt")
x = originalnumbers.readline()
while x != "":
    print(isEven(x))
    print(isOdd(x))
    print(isPrime(x))