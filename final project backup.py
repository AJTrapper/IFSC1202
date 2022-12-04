a = []
for i in range(23):
    a.append([' '] * (23))
for i in range(0,22):
# left column
	a[i][0] = '|'
# right column
	a[i][22] = '|'
#  upper row
	a[20][i] = '-'
# lower row	
	a[22][i] = '-'
# Corners
a[0][0]="+"
a[0][22] ="+"
a[22][0]="+"
a[22][22]="+"

