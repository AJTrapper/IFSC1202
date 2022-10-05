def isEven(x):
    if x%2==0:
        return True
    else:
        return False
originalnumbers = open("test function.txt")
x = originalnumbers.readline()
while x != "":
    isEven(x)
    print(res)