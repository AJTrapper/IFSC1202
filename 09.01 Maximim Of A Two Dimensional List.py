x = input("Enter the number of rows and columns: ")
y = x.split()
rows = int(y[0])
columns = int(y[1])
max = 0
a = []
for i in range(rows):
    a.append([0] * columns)

for i in range(rows):
    x = input("Enter a line of data: ")
    y = x.split()
    for j in range (columns):
        a[i][j] = int(y[j])

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


max = a[0][0]
maxrow = 0
maxcol = 0

for i in range(rows):
    for j in range(columns):
        if a[i][j] > max:
            max = a[i][j]
            maxrow = i
            maxcol = j

print(max)
print(maxrow)
print(maxcol)

