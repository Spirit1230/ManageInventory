import os
import re
import Item

class Inventory :

    inventoryFileName = ""
    stockFileName = ""

    def __init__(self, _inventoryFileName) :
        self.inventoryFileName = _inventoryFileName
        self.stockFileName = "Stock" + _inventoryFileName
        if (os.path.isfile(_inventoryFileName) == False) :
            self.__CreateNewInventory()

    def SearchItem(self) :
        itemToFind = str(input("Please input the name of what you want to find : "))
        searchResults = self.__SearchInventory(itemToFind)    

        if (len(searchResults) == 0) :
            print("Could not find " + itemToFind + " in inventory")
        else :
            for result in searchResults :
                print()
                result.PrintItem()
                print(self.__GetStock(result.barcode) + " in stock")

    def AddItem(self) :
        newItem = Item.Item()

        while (len(self.__SearchInventory(newItem.barcode)) != 0) :
            print("Barcode is not unique, please input a unique barcode")
            newItem.SetBarcode()

        self.__AddToInventory(newItem.GetDetails(), self.__SetStock())

    def RemoveItem(self) :
        itemToRemove = str(input("Please input the name of what you want to remove : "))
        self.__RemoveFromInventory(itemToRemove)
        print(itemToRemove + " removed")

    def AddStock(self) :
        pass

    def RemoveStock(self) :
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

        if (re.match("\d+", toFind)) :
            for item in inventoryFile :
                checkItem = Item.Item(self.__FormatFromFile(item))
                if (toFind == checkItem.barcode) :
                    matchingItems.append(checkItem)
        else :
            for item in inventoryFile :
                checkItem = Item.Item(self.__FormatFromFile(item))
                if (re.search(toFind.lower(), checkItem.name.lower())) :
                    matchingItems.append(checkItem)
        
        inventoryFile.close()

        return matchingItems

    def __AddToInventory(self, itemToAdd, stockToAdd) :
        toWrite = ""

        for item in itemToAdd :
            toWrite = toWrite + item + ","

        toWrite = toWrite.strip(",")
        toWrite = toWrite + "\n"

        inventory = open(self.inventoryFileName, "a")
        inventory.write(toWrite)
        inventory.close()

        stockInventory = open(self.stockFileName, "a")
        stockInventory.write(itemToAdd[0] + "," + stockToAdd + "\n")
        stockInventory.close()

    def __RemoveFromInventory(self, itemToRemove) :
        itemBarcode = ""

        tempInventoryName = self.inventoryFileName + "(temp)"

        inventoryFile = open(self.inventoryFileName, "r")
        newInventoryFile = open(tempInventoryName, "w")

        for item in inventoryFile :
            checkItem = Item.Item(self.__FormatFromFile(item))
            if (checkItem.name.lower() != itemToRemove.lower()) :
                newInventoryFile.write(item)
            else :
                itemBarcode = checkItem.barcode

        inventoryFile.close()
        newInventoryFile.close()

        os.remove(self.inventoryFileName)
        os.rename(tempInventoryName, self.inventoryFileName)

        if (itemBarcode != "") :
            tempStockName = self.stockFileName + "(temp)"

            stockFile = open(self.stockFileName, "r")
            newStockFile = open(tempStockName, "w")

            for item in stockFile :
                itemDetails = self.__FormatFromFile(item)
                if (itemBarcode != itemDetails[0]) :
                    newStockFile.write(item)

            stockFile.close()
            newStockFile.close()

            os.remove(self.stockFileName)
            os.rename(tempStockName, self.stockFileName)

    def __AlterNumInStock(self, barcode, numToAdjust) :
        pass

    def __CreateNewInventory(self) :
        newInventory = open(self.inventoryFileName, "w")
        newInventory.write("Barcode,Name,Price\n")
        newInventory.close()

        newStock = open(self.stockFileName, "w")
        newStock.write("Barcode,NumInStock\n")
        newStock.close()
        pass

    def __SetStock(self) :
        numberInStock = str(input("Number in stock : "))

        while (self.__IsStockValid(numberInStock) == False) :
            print("Invalid number of stock")
            numberInStock = str(input("Number in stock : "))

        return numberInStock

    def __GetStock(self, barcode) :
        stockInventory = open(self.stockFileName, "r")
        numInStock = "0"

        for item in stockInventory :
            itemDetails = self.__FormatFromFile(item)
            if (itemDetails[0] == barcode) :
                numInStock = itemDetails[1]
                break
        
        return numInStock

    def __IsStockValid(self, inputStock) :
        isValid = False

        if (re.match("^\d+$", inputStock)) :
            if (int(inputStock) >= 0) :
                isValid = True
        
        return isValid

    def __FormatFromFile(self, toFormat) :
        formatedEntry = toFormat.strip()
        return formatedEntry.split(",")