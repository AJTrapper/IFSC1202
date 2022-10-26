def print_list(a):
    print(a[0][i], a[1][i], a[2][i], a[3][i])

def swap_columns(a, i, j):
    if i == 0 and j ==1:
        print(a[1][i], a[0][i], a[2][i], a[3][i])
    if i == 0 and j ==2:
        print(a[2][i], a[1][i], a[0][i], a[3][i])
    if i == 0 and j ==3:
        print(a[3][i], a[1][i], a[2][i], a[0][i])
    if i == 1 and j ==2:
        print(a[0][i], a[2][i], a[1][i], a[3][i])
    if i == 1 and j ==3:
        print(a[0][i], a[3][i], a[2][i], a[1][i])
    if i == 3 and j ==2:
        print(a[0][i], a[1][i], a[3][i], a[2][i])

x = input("Enter the Columns to Swap: ")
y = x.split()
i = int(y[0])
j = int(y[1])

NameFile = open("09.02 NumbersList.txt")
    