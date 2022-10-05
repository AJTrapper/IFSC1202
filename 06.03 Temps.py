fileF = open("06.03 FTemps.txt")
fileC = open("06.03 CTemps.txt", "w") 
x = fileF.readline()
while x != "":
    x = float(x)
    y = (x-32)*5/9
    fileC.write("{:5.1f}".format(y) +"\n")
    x = fileF.readline()