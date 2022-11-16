class Retailitem ():

    def __init__(self, Description, UnitsOnHand, Price):


        self.itemDescription = Description
        self.itemUnitsOnHand = UnitsOnHand
        self.itemPrice = Price
    
    def IventoryValue(self):
        x = (self.itemUnitsOnHand)*(self.itemPrice)
        return x


print_inventory = []
RetailFile = open("11.01 Inventory.txt")
x = ReadFile.readline()
while x !="":
    y = x.split(",")
    MyRetail= Retail(y[0].strip(), y[1].strip(), int(y[2]), float(y[3]))
    print_inventory.


EmployeeLists = []
EmployeeFile = open("11.02 Employees.txt")
x = EmployeeFile.readline()
while x != "":
    y = x.split(",")
    MyEmployee = Employee(y[0].strip(), y[1].strip(), int(y[2]), float(y[3]))
    EmployeeLists.append(MyEmployee)
    x = EmployeeFile.readline()
EmployeeFile.close()




print("{:>10s} {:>10s} {:>10s} {:>10}".format( "Description", "Units On Hand", "Price", "Inventory Value"))
