import Inventory
import Item

class Checkout :

    storeInventory = None
    shoppingList = []

    def __init__(self, _storeInventoryLink) -> None:
        #class constructor
        self.storeInventory = Inventory.Inventory(_storeInventoryLink) #links checkout to inventory

    def ScanItem(self) :
        #Takes input from the user and adds the specified item to the list
        productName = str(input("Please input the products name : "))

        itemToBuy = self.storeInventory.SearchItem(productName)

        if (len(itemToBuy) == 0) :
            print("No item found")
        else :
            if (len(itemToBuy) > 1) :
                for item in itemToBuy :
                    print()
                    print(item.barcode)
                    item.PrintItem()

                itemBarcode = str(input("Please enter the correct items barcode : "))
            
            else :
                itemBarcode = itemToBuy[0].barcode

            numInStock = self.storeInventory.GetStock(itemBarcode)

            print("We have " + numInStock + " in stock")
            

    def PrintReceipt(self) :
        #Takes the items from the list and prints out a receipt
        pass

    def GetTotalPrice(self) :
        #Adds the price of all the items on the list and returns the value
        pass