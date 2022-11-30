from math import sqrt
from math import pi
from math import acos
class Triangle ():
	

    def __init__(self):


        self.S1 = 0
        self.S2 = 0
        self.S3 = 0

    def Type(self):
        if triangle1.S1 == triangle1.S2 == triangle1.S3:
            z = "Equailateral"
        if triangle1.S1 != triangle1.S2 != triangle1.S3:
            z = "Scalene"
        else:
            z = "Isocelese"
        return z


TriangleInfo = open("Exam Three Triangle.txt")
x = TriangleInfo.readline()
y = x.split(",")

triangle1 = Triangle()
triangle1.Type = z
triangle1.S1 = int(y[0].strip())
triangle1.S2 = int(y[1].strip())
triangle1.S3 = int(y[2].strip())
triangle1.Perimeter = (triangle1.S1) + (triangle1.S2) + (triangle1.S3)
s = (triangle1.Perimeter) * (1/2)
triangle1.Area = sqrt((s)*(s-(triangle1.S1))*(s-(triangle1.S2))*(s-(triangle1.S3)))
triangle1.Angle1 = acos((((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S2*triangle1.S3)))*(180/pi)
triangle1.Angle2 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S3)*(180/pi))
triangle1.Angle3 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S2)*(180/pi))
x = TriangleInfo.readline()
y = x.split(",")

triangle2 = Triangle()
triangle2.S1 = int(y[0].strip())
triangle2.S2 = int(y[1].strip())
triangle2.S3 = int(y[2].strip())
triangle2.Perimeter = (triangle1.S1) + (triangle1.S2) + (triangle1.S3)
s = (triangle1.Perimeter) * (1/2)
triangle2.Area = sqrt((s)*(s-(triangle1.S1))*(s-(triangle1.S2))*(s-(triangle1.S3)))
triangle2.Angle1 = acos((((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S2*triangle1.S3)))*(180/pi)
triangle2.Angle2 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S3)*(180/pi))
triangle2.Angle3 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S2)*(180/pi))
x = TriangleInfo.readline()
y = x.split(",")

triangle3 = Triangle()
triangle3.S1 = int(y[0].strip())
triangle3.S2 = int(y[1].strip())
triangle3.S3 = int(y[2].strip())
triangle3.Perimeter = (triangle1.S1) + (triangle1.S2) + (triangle1.S3)
s = (triangle1.Perimeter) * (1/2)
triangle3.Area = sqrt((s)*(s-(triangle1.S1))*(s-(triangle1.S2))*(s-(triangle1.S3)))
triangle3.Angle1 = acos((((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S2*triangle1.S3)))*(180/pi)
triangle3.Angle2 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S3)*(180/pi))
triangle3.Angle3 =acos(((triangle1.S1**2)+(triangle1.S2**2)+(triangle1.S3**2))/(2*triangle1.S1*triangle1.S2)*(180/pi))
x = TriangleInfo.readline()
y = x.split(",")

print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10} {:>10}".format( "Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
print("{:>10s} {:>10d} {:>10d} {:>10d} {:>10d} {:>10s} {:>10.3f} {:>10.3f} {:>10.3f}".format( type, triangle1.S1, triangle1.S2, triangle1.S3, triangle1.Perimeter, triangle1.Area, triangle1.Angle1, triangle1.Angle2, triangle1.Angle2))
print("{:>10s} {:>10d} {:>10d} {:>10d} {:>10d} {:>10s} {:>10.3f} {:>10.3f} {:>10.3f}".format( type, triangle2.S1, triangle2.S2, triangle2.S3, triangle2.Perimeter, triangle2.Area, triangle2.Angle1, triangle2.Angle2, triangle2.Angle2))
print("{:>10s} {:>10d} {:>10d} {:>10d} {:>10d} {:>10s} {:>10.3f} {:>10.3f} {:>10.3f}".format( type, triangle3.S1, triangle3.S2, triangle3.S3, triangle3.Perimeter, triangle3.Area, triangle3.Angle1, triangle3.Angle2, triangle3.Angle2))