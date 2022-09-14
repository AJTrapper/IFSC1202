x = float(input("Enter From value : "))
FromUnit = input("Enter From Unit (in, ft, yd, mi): ")
ToUnit = input("Enter To Unit (in, ft, yd, mi): ")
if FromUnit != "in" and FromUnit != "ft" and FromUnit != "yd" and FromUnit != "mi":
    print("11Error")
if ToUnit != "in" and ToUnit != "ft" and ToUnit != "yd" and ToUnit != "mi":
    print("Error")

#in ==
if FromUnit == "in" and ToUnit == "in":
    print("{} in  =>  {} in".format(x,x))
if FromUnit == "in" and ToUnit == "ft":
    print("{} in  =>  {} ft".format(x,x/12))
if FromUnit == "in" and ToUnit == "yd":
    print("{} in  =>  {} yd".format(x,x/36))
if FromUnit == "in" and ToUnit == "mi":
    print("{} in  =>  {} mi".format(x,x/63360))

#ft ==
if FromUnit == "ft" and ToUnit == "ft":
    print("{} ft  =>  {} ft".format(x,x))
if FromUnit == "ft" and ToUnit == "in":
    print("{} ft  =>  {} in".format(x,x*12))
if FromUnit == "ft" and ToUnit == "yd":
    print("{} ft  =>  {} yd".format(x,x/3))
if FromUnit == "ft" and ToUnit == "mi":
    print("{} ft  =>  {} mi".format(x,x/5280))

#yd ==
if FromUnit == "yd" and ToUnit == "yd":
    print("{} yd  =>  {} yd".format(x,x))
if FromUnit == "yd" and ToUnit == "in":
    print("{} yd  =>  {} in".format(x,x*36))
if FromUnit == "yd" and ToUnit == "ft":
    print("{} yd  =>  {} ft".format(x,x*3))
if FromUnit == "yd" and ToUnit == "mi":
    print("{} yd  =>  {} mi".format(x,x/1760))

#mi ==
if FromUnit == "mi" and ToUnit == "mi":
    print("{} mi  =>  {} mi".format(x,x))
if FromUnit == "mi" and ToUnit == "in":
    print("{} mi  =>  {} in".format(x,x*63360))
if FromUnit == "mi" and ToUnit == "ft":
    print("{} mi  =>  {} ft".format(x,x*5280))
if FromUnit == "mi" and ToUnit == "yd":
    print("{} mi  =>  {} yd".format(x,x*1760))