import Checkout
import Inventory

if __name__ == "__main__" :

    print("Do you want to test :\n1. Inventory Controls\n2. Checkout")
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

        for num in range(0, 5) :
            checkout.ScanItem()
        checkout.PrintReceipt()
    else :
        print("Invalid input")