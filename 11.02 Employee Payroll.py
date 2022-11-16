class Employee ():
	

    def __init__(self, FirstName, LastName, IDNumber, Wage):


        self.employeeFirstName = FirstName
        self.employeeLastName = LastName
        self.employeeIDNumber = IDNumber
        self.employeeHoursWorked = 0.0
        self.employeeWage = Wage
    
    def WeeklyPay(self):
        if self.employeeHoursWorked > 40:
            x = ((self.employeeHoursWorked-40) *(1.5*self.employeeWage)) + (40*self.employeeWage)
        else:
            x = (self.employeeHoursWorked)* (self.employeeWage)
        return x

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
    MyEmployee = Employee(y[0].strip(), y[1].strip(), int(y[2]), float(y[3]))
    EmployeeLists.append(MyEmployee)
    x = EmployeeFile.readline()
EmployeeFile.close()

EmployeeHours = open("11.02 Hours.txt")
x = EmployeeHours.readline()
while x != "":
    y = x.split(",")
    employeeIDNumber = int((y[0]).strip())
    employeeHoursWorked = float((y[1]).strip())
    empidx = find_employee(EmployeeLists, employeeIDNumber)
    EmployeeLists[empidx].employeeHoursWorked = employeeHoursWorked
    x = EmployeeHours.readline()
EmployeeHours.close()    

print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "Name", "Name", "Number", "Worked", "Wage", "Pay"))

for i in range (len(EmployeeLists)):
    print("{:>10s} {:>10s} {:>10d} {:>10.2f} {:10.2f} {:10.2f}".format(EmployeeLists[i].employeeFirstName, EmployeeLists[i].employeeLastName, EmployeeLists[i].employeeIDNumber, EmployeeLists[i].employeeHoursWorked, EmployeeLists[i].employeeWage, EmployeeLists[i].WeeklyPay()))