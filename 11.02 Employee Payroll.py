class Employee ():
	

    def __init__(self, FirstName, LastName, IDNumber, Wage):


        self.employeeName = FirstName
        self.employeeLastName = LastName
        self.employeeIDNumber = IDNumber
        self.employeeHoursWorked = 0.0
        self.employeeWage = Wage
    
    def WeeklyPay(self):
        if self.HoursWorked > 40:
            x = ((self.HoursWorked -40) *(1.5*self.Wage)) + (40*self.Wage)
        else:
            x = (self.HoursWorked)* (self.Wage)
        self.WeeklyPay = x
        return self.WeeklyPay

def find_employee(EMPList, EMPID):
    for i in range(len(EMPList)):
        if EMPList[i].employeeIDNumber == EMPID:
            return i
    return -1


EmployeeLists = []
EmployeeFile = open("11.02 Employees.txt")
x = EmployeeFile.readline()
while x != "":
    y = x.split(",")
    MyEmployee = Employee(y[0], y[1], int(y[2]), float(y[3]))
    EmployeeLists.append(MyEmployee)
    x = EmployeeFile.readline()

EmployeeHours = open("11.02 Hours.txt")
x = EmployeeHours.readline()
while x != "":
    y = x.split(",")
    employeeIDNumber = int(y[0])
    employeeHoursWorked = float(y[1])
    empidx = find_employee(EmployeeLists, employeeIDNumber)
    EmployeeLists[empidx].employeeHoursWorked = employeeHoursWorked
    

print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "First", "Last", "ID", "Hours", "Houly", "Weekly"))
print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "Name", "Name", "Number", "Worked", "Wage", "Pay"))

