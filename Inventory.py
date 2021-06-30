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

def RemoveItem(fileName, barcode) :
    pass

def SearchItem(fileName, barcode) :
    pass

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
            pass
        elif (optionPicked == "2") :
            AddItem(inventoryName)
        elif (optionPicked == "3") :
            pass
        elif (optionPicked == "4") :
            accessingInventory = False
        else :
            print("Invalid input")