import Inventory

if __name__ == "__main__" :

    #creates instance of Inventory() class
    inventoryName = "StoreInventory.csv"
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