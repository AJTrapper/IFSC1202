

def percentchange (t,y):
    c = (t-y)/y*100
    return c

stockfile = open("06.02 Stock.txt")
x = stockfile.readline()
y = float(x)
print("{:>15s} {:>15s}".format("Stock", "Change"))
print("{:>15.2f}".format(float(x)))
x = stockfile.readline()  
while x != "":
    print("{:15.2f} {:15.2f}".format(float(x), percentchange(float(x), y)))
    y = float(x)
    x = stockfile.readline()