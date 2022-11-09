class Employee ():
	

    def __init__(self):


        self.employeeName = ""
        self.employeeLastName = ""
        self.employeeIDNumber = 0.0
        self.employeeHoursWorked = 0.0
        self.employeeWage = 0.0
EmployeeInfo = open("10.06 Payroll.txt")
x = EmployeeInfo.readline()
y = x.split(",")
employee1 = Employee()
employee1.Name = y[0].strip()
employee1.LastName = y[1].strip()
employee1.IDNumber = int(y[2].strip())
employee1.HoursWorked = float(y[3].strip())
employee1.Wage = float(y[4].strip())
if employee1.HoursWorked > 40:
    x = ((employee1.HoursWorked -40) *(1.5*employee1.Wage)) + (40*employee1.Wage)
else:
    x = (employee1.HoursWorked)* (employee1.Wage)
employee1.WeeklyPay = x

x = EmployeeInfo.readline()
y = x.split(",")
employee2 = Employee()
employee2.Name = y[0].strip()
employee2.LastName = y[1].strip()
employee2.IDNumber = int(y[2].strip())
employee2.HoursWorked = float(y[3].strip())
employee2.Wage = float(y[4].strip())
if employee2.HoursWorked > 40:
    x = ((employee2.HoursWorked -40) *(1.5*employee2.Wage)) + (40*employee2.Wage)
else:
    x = (employee2.HoursWorked)* (employee2.Wage)
employee2.WeeklyPay = x

x = EmployeeInfo.readline()
y = x.split(",")
employee3 = Employee()
employee3.Name = y[0].strip()
employee3.LastName = y[1].strip()
employee3.IDNumber = int(y[2].strip())
employee3.HoursWorked = float(y[3].strip())
employee3.Wage = float(y[4].strip())
if employee3.HoursWorked > 40:
    x = ((employee3.HoursWorked -40) *(1.5*employee3.Wage)) + (40*employee3.Wage)
else:
    x = (employee3.HoursWorked)* (employee3.Wage)
employee3.WeeklyPay = x

EmployeeInfo.close()

print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "First", "Last", "ID", "Hours", "Houly", "Weekly"))
print("{:>10s} {:>10s} {:>10s} {:>10} {:>10s} {:>10}".format( "Name", "Name", "Number", "Worked", "Wage", "Pay"))
print("{:>10s} {:>10s} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f}".format( employee1.Name, employee1.LastName, employee1.IDNumber, employee1.HoursWorked, employee1.Wage, employee1.WeeklyPay))
print("{:>10s} {:>10s} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f}".format( employee2.Name, employee2.LastName, employee2.IDNumber, employee2.HoursWorked, employee2.Wage, employee2.WeeklyPay))
print("{:>10s} {:>10s} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f}".format( employee3.Name, employee3.LastName, employee3.IDNumber, employee3.HoursWorked, employee3.Wage, employee3.WeeklyPay))