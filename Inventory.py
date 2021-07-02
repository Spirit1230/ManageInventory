import os
import re
import Item

class Inventory :

    inventoryFileName = ""

    def __init__(self, _inventoryFileName) :
        if (os.path.isfile(_inventoryFileName) == False) :
            self.__CreateNewInventory(_inventoryFileName)
        self.inventoryFileName = _inventoryFileName

    def SearchItem(self) :
        itemToFind = str(input("Please input the name of what you want to find : "))
        searchResults = self.__SearchInventory(itemToFind)    

        if (len(searchResults) == 0) :
            print("Could not find " + itemToFind + " in inventory")
        else :
            for result in searchResults :
                print()
                result.PrintItem()

    def AddItem(self) :
        item = Item.Item()    
        self.__AddToInventory(item.GetDetails())

    def RemoveItem(self) :
        itemToRemove = str(input("Please input the name of what you want to remove : "))
        self.__RemoveFromInventory(itemToRemove)
        print(itemToRemove + " removed")

    def IncrementStock(self) :
        pass

    def DisplayOptions(self) :
        print("-------------------------------------")
        print("Hello what do you want to do today?\n")
        print("1. Search for an item")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Exit")
        print("-------------------------------------")

    def __SearchInventory(self, toFind) :
        inventoryFile = open(self.inventoryFileName, "r")
        matchingItems = []

        for item in inventoryFile :
            checkItem = Item.Item(item.split(","))
            if (re.search(toFind.lower(), checkItem.name.lower())) :
                matchingItems.append(checkItem)
        
        inventoryFile.close()

        return matchingItems

    def __AddToInventory(self, itemToAdd) :
        toWrite = ""

        for item in itemToAdd :
            toWrite = toWrite + item + ","

        toWrite = toWrite.strip(",")
        toWrite = toWrite + "\n"

        inventory = open(self.inventoryFileName, "a")
        inventory.write(toWrite)
        inventory.close()

    def __RemoveFromInventory(self, itemToRemove) :
        tempInventoryName = self.inventoryFileName + "(temp)"

        inventoryFile = open(self.inventoryFileName, "r")
        newInventoryFile = open(tempInventoryName, "w")

        for item in inventoryFile :
            checkItem = Item.Item(item.split(","))
            if (checkItem.name.lower() != itemToRemove.lower()) :
                newInventoryFile.write(item)

        inventoryFile.close()
        newInventoryFile.close()

        os.remove(self.inventoryFileName)
        os.rename(tempInventoryName, self.inventoryFileName)

    def __CreateNewInventory(self) :
        newInventory = open(self.inventoryFileName, "w")
        newInventory.write("Barcode,Name,Price,NumInStock\n")
        newInventory.close()
        pass