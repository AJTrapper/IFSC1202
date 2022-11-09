class Car ():
    def __init__(self):


        self.carYear = 0
        self.carMake = ""
        self.carSpeed = 0.0
CarInfo = open("10.03 Cars.txt")
x = CarInfo.readline(0)
y = x.split(",")
car1 = Car()
car1.Year = y[0].strip()
car1.Make = y[1].strip()

CarInfo = open("10.03 Cars.txt")
x = CarInfo.readline(1)
y = x.split(",")
car1 = Car()
car1.Speed = int(y[0].strip())

CarInfo = open("10.03 Cars.txt")
x = CarInfo.readline(1)
y = x.split(",")
car1 = Car()
car1.Speed = int(y[0].strip())

print("{:>10s} {:>10s}".format("Make :", car1.Make))
print("{:>10s} {:>10d}".format("Year :", car1.Year))
print(" ")
print("{:>10s} {:>10s}".format("Change", "Speed"))