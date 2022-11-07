
class RetailItem ():
	

    def __init__(self):


        self.itemDescription = ""
        self.itemUnitsOnHand = 0
        self.itemPrice = 0.0
RetailInfo = open("10.02 Inventory.txt")
x = RetailInfo.readline()
y = x.split(",")
item1 = RetailItem()
item1.Description = y[0].strip()
item1.UnitsOnHand = int(y[1].strip())
item1.Price = float(y[2].strip())
item1.InventoryValue = (item1.UnitsOnHand) * (item1.Price)
x = RetailInfo.readline()
y = x.split(",")
item2 = RetailItem()
item2.Description = y[0].strip()
item2.UnitsOnHand = int(y[1].strip())
item2.Price = float(y[2].strip())
item2.InventoryValue = (item2.UnitsOnHand) * (item2.Price)
x = RetailInfo.readline()
y = x.split(",")
item3 = RetailItem()
item3.Description = y[0].strip()
item3.UnitsOnHand = int(y[1].strip())
item3.Price = float(y[2].strip())
item3.InventoryValue = (item3.UnitsOnHand) * (item3.Price)
RetailInfo.close()
print("{:>10s} {:>10s} {:>10s} {:>10}".format( "Description", "Units On Hand", "Price", "Inventory Value"))
print("{:>10s} {:>10d} {:>16.2f} {:>16.2f}".format( item1.Description, item1.UnitsOnHand, item1.Price, item1.InventoryValue))
print("{:>10s} {:>10d} {:>16.2f} {:>16.2f}".format( item2.Description, item2.UnitsOnHand, item2.Price, item2.InventoryValue))
print("{:>10s} {:>10d} {:>16.2f} {:>16.2f}".format( item3.Description, item3.UnitsOnHand, item3.Price, item3.InventoryValue))
