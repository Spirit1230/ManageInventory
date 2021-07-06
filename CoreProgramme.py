import Checkout
import Inventory
import StockCheckerApp

if __name__ == "__main__" :

    print("Do you want to test :\n1. Inventory Controls\n2. Checkout\n3. Stock Checker App")
    choice = str(input())

    inventoryName = "StoreInventory.csv"

    if (choice == "1") :
        #creates instance of Inventory() class
        storeInventory = Inventory.Inventory(inventoryName)

        accessingInventory = True

        #interface for interacting with the Inventory() class
        while accessingInventory :
            storeInventory.DisplayOptions()
            optionPicked = str(input("Please pick an option : "))

            if (optionPicked == "1") :
                storeInventory.SearchItem()
            elif (optionPicked == "2") :
                storeInventory.AddItem()
            elif (optionPicked == "3") :
                storeInventory.RemoveItem()
            elif (optionPicked == "4") :
                storeInventory.AddStock()
            elif (optionPicked == "5") :
                storeInventory.RemoveStock()
            elif (optionPicked == "6") :
                accessingInventory = False
            else :
                print("Invalid input")
    elif (choice == "2") :
        checkout = Checkout.Checkout(inventoryName)

        scanNextItem = True
        while scanNextItem :
            checkout.ScanItem()
            continueScanning = str(input("Do you want to scan another item? (y/n) : "))
            if (continueScanning.lower() != "y") :
                scanNextItem = False
                
        checkout.TakePayment()
    elif (choice == "3") :
        stockChecker = StockCheckerApp.StockChecker(inventoryName)
        usingApp = True

        while usingApp :
            stockChecker.FindItem()
            findAnotherItem = str(input("Do you want to find another item? (y/n) : "))
            if (findAnotherItem.lower() != "y") :
                usingApp = False
    else :
        print("Invalid input")