import os
import Item

def AddItem(fileName) :
    item = Item.Item()
    itemDetails = item.GetDetails()

    toWrite = ""

    for item in itemDetails :
        toWrite = toWrite + item + ","

    toWrite = toWrite.strip(",")
    toWrite = toWrite + "\n"

    inventory = open(fileName, "a")
    inventory.write(toWrite)
    inventory.close()

def RemoveItem(fileName) :
    pass

def SearchItem(fileName) :
    itemToFind = str(input("Please input the name of what you want to find :"))

    foundItem = False
    inventoryFile = open(fileName, "r")

    for item in inventoryFile :
        checkItem = Item.Item(item.split(","))
        if (checkItem.name.lower() == itemToFind.lower()) :
            checkItem.PrintItem()
            foundItem = True
            break
    
    inventoryFile.close()

    if (foundItem == False) :
        print("Could not find " + itemToFind + " in inventory")


def CreateNewInventory(fileName) :
    newInventory = open(fileName, "w")
    newInventory.write("Barcode,Name,Price,NumInStock\n")
    newInventory.close()
    pass

def DisplayOptions() :
    print("-------------------------------------")
    print("Hello what do you want to do today?\n")
    print("1. Search for an item")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Exit")
    print("-------------------------------------")

if __name__ == "__main__" :
    inventoryName = "StoreInventory.csv"

    if (os.path.isfile(inventoryName) != True) :
        CreateNewInventory(inventoryName)
    else :
        print("Inventory already exists")

    accessingInventory = True

    while accessingInventory :
        DisplayOptions()
        optionPicked = str(input("Please pick an option : "))

        if (optionPicked == "1") :
            SearchItem(inventoryName)
        elif (optionPicked == "2") :
            AddItem(inventoryName)
        elif (optionPicked == "3") :
            pass
        elif (optionPicked == "4") :
            accessingInventory = False
        else :
            print("Invalid input")