a = int(input("Enter A:"))
b = int(input("Enter B: "))
for j in range(a,b+1):
    for i in range (2,(j // 2)  + 1):
        if (j%i)==0:
            break
    else:
        print(j)