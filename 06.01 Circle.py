from math import pi
def diameter(r):
    d = 2 * r
    return d

def circumference(r):
    c = 2 * pi * r
    return c

def area(r):
    a = pi * (r**2)
    return a

radiusfile = open("06.01 Radius.txt.")
x = radiusfile.readline()
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter","Circumference", "Area"))
while x != "":
# Print the contents - Note the embedded linefeeds
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(float(x), diameter(float(x)), circumference(float(x)), area(float(x))))  
    x = radiusfile.readline()






