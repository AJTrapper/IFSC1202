x = int(input("Enter NUmber N :"))
for i in range (2,(x // 2)  + 1):
    if (x%i)==0:
      print("Composite")
      break
else:
    print("Prime")