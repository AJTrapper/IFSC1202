
n = int(input("Enter the number of rows and columns: "))
a= []

for i in range(n+2):
    a.append([' '] * (n+2))
for i in range(1,n+1):
# left column
	a[i][0] = '|'
# right column
	a[i][n+1] = '|'
##  upper row
	a[0][i] = '-'
# lower row	
	a[n+1][i] = '-'
# Corners
a[0][0]="+"
a[0][n+1] ="+"
a[n+1][0]="+"
a[n+1][n+1]="+"

for i in range(1,n+1,2):
    for j in range(1,n+1,2):
        a[i][j] = "*"
    

for i in range(2,n+1,2):
    for j in range(2,n+1,2):
        a[i][j] = "*"
    

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()