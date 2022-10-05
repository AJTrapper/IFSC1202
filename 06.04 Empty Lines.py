inputfile = open("06.04 EmptyLinesInput.txt")
outputfile = open("06.04 EmptyLinesOutput.txt", "w")
r = 0
w = 0
x = inputfile.readline()
while x != "":
    r = r+1
    if x != "\n":
        outputfile.write(x)
        w = w+1
    x = inputfile.readline()
print("{} Records Read".format(r))
print("{} Records Written".format(w))