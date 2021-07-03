import os
import re
import Item

class Inventory :

    inventoryFileName = ""
    stockFileName = ""

    def __init__(self, _inventoryFileName) :
        #class constructor
        self.inventoryFileName = _inventoryFileName
        self.stockFileName = "Stock" + _inventoryFileName
        if (os.path.isfile(_inventoryFileName) == False) :
            #creates two new files if the appropriate files are missing
            self.__CreateNewInventory()

    def SearchItem(self) :
        #searches for an item in the inventory file and prints the result

        #takes input from the user and then searches the inventory file
        itemToFind = str(input("Please input the name of what you want to find : "))
        searchResults = self.__SearchInventory(itemToFind)    

        if (len(searchResults) == 0) :
            #no results found
            print("Could not find " + itemToFind + " in inventory")
        else :
            #prints all results that match the search criteria
            #the result variable will be an instance of the Item class
            for result in searchResults :
                print()
                result.PrintItem()
                print(self.GetStock(result.barcode) + " in stock")

    def AddItem(self) :
        #adds a new item to the inventory and stock files

        #creates a new item
        newItem = Item.Item()

        #checks the barcode provided is unique otherwise it asks for another barcode
        while (len(self.__SearchInventory(newItem.barcode)) != 0) :
            print("Barcode is not unique, please input a unique barcode")
            newItem.SetBarcode()

        #acquires the amount of stock available
        numInStock = self.__SetStock()

        #adds new item to files
        self.__AddToInventory(newItem.GetDetails(), numInStock)

    def RemoveItem(self) :
        #removes an item from the inventory and stock files

        #acquires the name for the item to remove
        itemToRemove = str(input("Please input the name of what you want to remove : "))

        #checks the inentory for the item and pulls up all valid results
        itemsToRemove = self.__SearchInventory(itemToRemove)

        for item in itemsToRemove :
            print()
            print(item.barcode)
            item.PrintItem()

        #acquires the barcode for the item to remove
        barcodeToRemove = str(input("Please input the barcode of the item you wish to remove : "))

        #removes the item from both files
        self.__RemoveFromInventory(barcodeToRemove)
        print(itemToRemove + " removed")

    def AddStock(self) :
        #adds stock to a specified item

        #gets the items barcode from the user
        barcode = str(input("Please enter the barcode of the item to adjust : "))

        #gets the amount of stock to add from the user
        numToAdd = str(input("Please enter the number of stock to add : "))

        #keeps asking for the amount of stock until a valid input
        while (self.__IsStockValid(numToAdd) == False) :
            print("Invalid input")
            numToAdd = str(input("Please enter the number of stock to add : "))

        #adjusts the specified items stock
        self.__AlterNumInStock(barcode, int(numToAdd))

    def RemoveStock(self) :
        #removes stock from a specified item

        #acquires barcode from user
        barcode = str(input("Please enter the barcode of the item to adjust : "))

        #acquires amount of stock to remove from user
        numToRemove = str(input("Please enter the number of stock to add : "))

        #keeps asking until a valid input
        while (self.__IsStockValid(numToRemove) == False) :
            print("Invalid input")
            numToRemove = str(input("Please enter the number of stock to add : "))

        #alters the specified items stock
        self.__AlterNumInStock(barcode, -int(numToRemove))
    
    def GetStock(self, barcode) :
        #gets the stock of a specified item
        stockInventory = open(self.stockFileName, "r")
        numInStock = "0"

        #cycles through stock file until the specified barcode is reached
        for item in stockInventory :
            itemDetails = self.__FormatFromFile(item)
            if (itemDetails[0] == barcode) :
                numInStock = itemDetails[1]
                break
        
        return numInStock

    def DisplayOptions(self) :
        #displays all the options for interacting with the inventory class
        print("-------------------------------------")
        print("Hello what do you want to do today?\n")
        print("1. Search for an item")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Add stock")
        print("5. Remove stock")
        print("6. Exit")
        print("-------------------------------------")

    def __SearchInventory(self, toFind) :
        #finds all items that match toFind in the inventory and returns a list of Items()

        inventoryFile = open(self.inventoryFileName, "r")
        matchingItems = []

        if (re.match("\d+", toFind)) :
            #if toFind is a barcode
            for item in inventoryFile :
                #cycles through inventory checking each items barcode
                checkItem = Item.Item(self.__FormatFromFile(item))
                if (toFind == checkItem.barcode) :
                    #adds valid item to list
                    matchingItems.append(checkItem)
        else :
            #if toFind is a name
            for item in inventoryFile :
                #cycles through inventory checking each items name
                checkItem = Item.Item(self.__FormatFromFile(item))
                if (re.search(toFind.lower(), checkItem.name.lower())) :
                    #adds valid item to list
                    matchingItems.append(checkItem)
        
        inventoryFile.close()

        #returns the list of Item()
        return matchingItems

    def __AddToInventory(self, itemToAdd, stockToAdd) :
        #adds an item and its stock to the appropriate files

        #compiles the item details to add to the inventory file
        toWrite = ""

        for item in itemToAdd :
            toWrite = toWrite + item + ","

        #removes trailing "," and adds a newline 
        toWrite = toWrite.strip(",")
        toWrite = toWrite + "\n"

        #appends details to inventory file
        inventory = open(self.inventoryFileName, "a")
        inventory.write(toWrite)
        inventory.close()

        #appends stock to stock file
        stockInventory = open(self.stockFileName, "a")
        stockInventory.write(itemToAdd[0] + "," + stockToAdd + "\n")
        stockInventory.close()

    def __RemoveFromInventory(self, barcodeToRemove) :
        #removes an item from the inventory and stock files

        #creates new inventory file with a temporary name
        tempInventoryName = "(temp)" + self.inventoryFileName

        inventoryFile = open(self.inventoryFileName, "r")
        newInventoryFile = open(tempInventoryName, "w")

        #cycles through moving all entries from the old file to the new one bar the entry to remove
        for item in inventoryFile :
            checkItem = Item.Item(self.__FormatFromFile(item))
            if (checkItem.barcode != barcodeToRemove) :
                newInventoryFile.write(item)

        inventoryFile.close()
        newInventoryFile.close()

        #removes the old file and renames the new one to the original file name
        os.remove(self.inventoryFileName)
        os.rename(tempInventoryName, self.inventoryFileName)

        #creates a new stock file with a temporary name
        tempStockName = "(temp)" + self.stockFileName

        stockFile = open(self.stockFileName, "r")
        newStockFile = open(tempStockName, "w")

        #cycles through moving all entries from the old file to the new one bar the entry to remove
        for item in stockFile :
            itemDetails = self.__FormatFromFile(item)
            if (barcodeToRemove != itemDetails[0]) :
                newStockFile.write(item)

        stockFile.close()
        newStockFile.close()

        #removes the old file and renames the new one to the original file name
        os.remove(self.stockFileName)
        os.rename(tempStockName, self.stockFileName)

    def __AlterNumInStock(self, barcode, numToAdjust) :
        #adjust the amount of stock an item has

        #creates a new stock file with a temporary name
        tempStockInventory = "(temp)" + self.stockFileName

        stockInventory = open(self.stockFileName, "r")
        newStockInventory = open(tempStockInventory, "w")

        #cycles through adding all entries from the old file to the new one
        for item in stockInventory :
            itemDetails = self.__FormatFromFile(item)
            if (barcode != itemDetails[0]) :
                newStockInventory.write(item)
            else :
                #alters the specified items stock
                numInStock = int(itemDetails[1])
                adjustedStock = numInStock + numToAdjust
                if (adjustedStock < 0) :
                    #sets stock to zero if new stock falls below zero
                    adjustedStock = 0
                newStockInventory.write(itemDetails[0] + "," + str(adjustedStock) + "\n")

        stockInventory.close()
        newStockInventory.close()

        #removes old file and renames new one to the original file name
        os.remove(self.stockFileName)
        os.rename(tempStockInventory, self.stockFileName)

    def __CreateNewInventory(self) :
        #creates new inventory and stock files

        #creates a new inventory file with header
        newInventory = open(self.inventoryFileName, "w")
        newInventory.write("Barcode,Name,Price\n")
        newInventory.close()

        #creates a new stock file with header
        newStock = open(self.stockFileName, "w")
        newStock.write("Barcode,NumInStock\n")
        newStock.close()
        pass

    def __SetStock(self) :
        #gets input from the user for the items stock
        numberInStock = str(input("Number in stock : "))

        #continues to ask for input until a valid input is given
        while (self.__IsStockValid(numberInStock) == False) :
            print("Invalid number of stock")
            numberInStock = str(input("Number in stock : "))

        return numberInStock

    def __IsStockValid(self, inputStock) :
        #checks input stock is valid
        isValid = False

        #stock must be a positive whole number
        if (re.match("^\d+$", inputStock)) :
            if (int(inputStock) >= 0) :
                isValid = True
        
        return isValid

    def __FormatFromFile(self, toFormat) :
        #formats lines from the files
        formatedEntry = toFormat.strip() #removes all trailing whitespace (eg newlines)
        return formatedEntry.split(",") #splits by "," to return entries as lists