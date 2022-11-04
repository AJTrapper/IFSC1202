
class RetailItem ():
	

    def __init__(self):


        self.itemDescription = ""
        self.itemUnitsOnHand = 0
        self.itemPrice = 0
RetailInfo = open("10.02 Inventory.txt")
x = RetailInfo.readline()
y = x.split(",")
item1 = RetailItem()
item1.Description = y[0].strip()
item1.UnitsOnHand = int(y[1].strip())
item1.Price = int(y[2].strip())
x = PetInfo.readline()
y = x.split(",")
item2 = RetailItem()
item2.Description = y[0].strip()
item2.UnitsOnHand = int(y[1].strip())
item2.Price = int(y[2].strip())
x = PetInfo.readline()
y = x.split(",")
item3 = RetailItem()
item3.Description = y[0].strip()
itewm3.UnitsOnHand = int(y[1].strip())
item3.Price = int(y[2].strip())
PetInfo.close()
print("{:>8s} {:>8s} {:>8s}".format( "Description", "Units On Hand", "Price"))
print("{:>8s} {:>8s} {:>8d}".format( item1.Description, item1.UnitsOnHand, item1.Price))
print("{:>8s} {:>8s} {:>8d}".format( item2.Description, item2.UnitsOnHand, item2.Price))
print("{:>8s} {:>8s} {:>8d}".format( item3.Description, item3.UnitsOnHand, item3.Price))
