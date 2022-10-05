fileA = open("06.05 CompareFileA.txt")
fileB = open("06.05 CompareFileB.txt")
x = fileA.readline()
y = fileB.readline()
d = 0
l = 0
while x != "":
    l = l+1
    if x != y:
        print("Line: {} -File A {}".format(l,x))
        print("Line: {} -File B {}".format(l,y))
        d= d+1
    x = fileA.readline()
    y = fileB.readline()
print("{} Differences".format(d))