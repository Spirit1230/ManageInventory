import Inventory

class Checkout :

    storeInventory = None
    shoppingList = []

    def __init__(self, _storeInventoryLink) -> None:
        #class constructor
        self.storeInventory = Inventory.Inventory(_storeInventoryLink) #links checkout to inventory

    def ScanItem(self) :
        #Takes input from the user and adds the specified item to the list
        self.storeInventory.SearchItem()

        itemBarcode = str(input("Please input the barcode of the item to scan : "))
        itemScanned = self.storeInventory.GetItem(itemBarcode)
        numInStock = self.storeInventory.GetStock(itemBarcode)

        if (numInStock == "0") :
            print("Item not available")
        else :
            self.shoppingList.append(itemScanned)            

    def PrintReceipt(self) :
        #Takes the items from the list and prints out a receipt
        print()
        print("Item".ljust(30) + "Price /£")
        for item in self.shoppingList :
            name = str(item[1])
            price = str(item[2])
            print(name.ljust(30) + price)
        print()
        print("Total".ljust(30) + str(self.__CalculateTotalPrice()))
        print()
        pass

    def __CalculateTotalPrice(self) :
        #Adds the price of all the items on the list and returns the value
        totalPrice = 0

        for item in self.shoppingList :
            itemPrice = float(item[2])
            totalPrice = totalPrice + itemPrice

        return "{:.2f}".format(totalPrice)