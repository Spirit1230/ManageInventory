import os
import re
import Item

class Inventory :

    inventoryFileName = ""
    stockFileName = ""
    locationFileName = ""

    def __init__(self, _inventoryFileName) :
        #class constructor
        self.inventoryFileName = _inventoryFileName
        self.stockFileName = "Stock" + _inventoryFileName
        self.locationFileName = "Location" + _inventoryFileName
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
                print("Located at " + self.GetLocation(result.barcode))

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

        #acquires where the item can be found in the store
        location = str(input("Please enter where the item is located in store : "))

        #adds new item to files
        self.__AddToInventory(newItem.GetDetails(), numInStock, location)

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

        #removes the item from all files
        self.__RemoveItemFromFile(barcodeToRemove, self.inventoryFileName)
        self.__RemoveItemFromFile(barcodeToRemove, self.stockFileName)
        self.__RemoveItemFromFile(barcodeToRemove, self.locationFileName)
        print(itemToRemove + " removed")

    def AddStock(self, barcode = None, numToAdd = None) :
        #adds stock to a specified item

        #gets the items barcode from the user
        if (barcode == None) :
            barcode = str(input("Please enter the barcode of the item to adjust : "))
        else :
            barcode = str(barcode)

        #gets the amount of stock to add from the user
        if (numToAdd == None) :
            numToAdd = str(input("Please enter the number of stock to add : "))
        else :
            numToAdd = str(numToAdd)

        #keeps asking for the amount of stock until a valid input
        while (self.__IsStockValid(numToAdd) == False) :
            print("Invalid input")
            numToAdd = str(input("Please enter the number of stock to add : "))

        #adjusts the specified items stock
        self.__AlterNumInStock(barcode, int(numToAdd))

    def RemoveStock(self, barcode = None, numToRemove = None) :
        #removes stock from a specified item

        #acquires barcode from user
        if (barcode == None) :
            barcode = str(input("Please enter the barcode of the item to adjust : "))
        else :
            barcode = str(barcode)

        #acquires amount of stock to remove from user
        if (numToRemove == None) :
            numToRemove = str(input("Please enter the number of stock to add : "))
        else :
            numToRemove = str(numToRemove)

        #keeps asking until a valid input
        while (self.__IsStockValid(numToRemove) == False) :
            print("Invalid input")
            numToRemove = str(input("Please enter the number of stock to add : "))

        #alters the specified items stock
        self.__AlterNumInStock(barcode, -int(numToRemove))

    def ChangeLocation(self, barcode = None, newLoaction = None) :
        #Changes the location an item can be found in

        #Gets input from the user if no barcode has been specified
        if (barcode == None) :
            barcode = str(input("Please enter the barcode of the item to adjust :"))
        else :
            barcode = str(barcode)

        #Gets a new location from the user if no location is specified
        if (newLoaction == None) :
            newLoaction = str(input("Please enter the items new location : "))
        else :
            newLoaction = str(newLoaction)

        #removes the old entry and replaces it with the updated one
        self.__RemoveItemFromFile(barcode, self.locationFileName)

        locationFile = open(self.locationFileName, "a")
        locationFile.write(barcode + "," + newLoaction + "\n")
        locationFile.close()
    
    def GetItem(self, barcode = None) :

        #gets barcode from user
        if (barcode == None) :
            barcode = str(input("Please enter the barcode for the item you want : "))
        else :
            barcode = str(barcode)

        #gets the specified item
        itemInventory = open(self.inventoryFileName, "r")
        itemToGet = []

        #cycles through inventory until specified barcode is reached
        for item in itemInventory :
            itemDetails = self.__FormatFromFile(item)
            if (itemDetails[0] == barcode) :
                itemToGet = itemDetails
                break
        
        return itemToGet

    def GetStock(self, barcode = None) :
        #gets barcode from user
        if (barcode == None) :
            barcode = str(input("Please enter the barcode for the item you want : "))
        else :
            barcode = str(barcode)

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

    def GetLocation(self, barcode = None) :
        #gets barcode from user
        if (barcode == None) :
            barcode = str(input("Please enter the barcode for the item you want : "))
        else :
            barcode = str(barcode)

        #gets the location of the specified item
        locationInventory = open(self.locationFileName, "r")
        location = "Item not found"

        #cycles through location file until the specified barcode is reached
        for item in locationInventory :
            itemDetails = self.__FormatFromFile(item)
            if (itemDetails[0] == barcode) :
                location = itemDetails[1]
                break
        
        return location

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

        toFind = str(toFind)

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

    def __AddToInventory(self, itemToAdd, stockToAdd, locatedAt) :
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

        #appends location to location file
        stockInventory = open(self.locationFileName, "a")
        stockInventory.write(itemToAdd[0] + "," + locatedAt + "\n")
        stockInventory.close()

    def __RemoveItemFromFile(self, barcodeToRemove, fileName) :
        #removes an item from the specified file

        #creates a new temporary name
        tempFileName = "(temp)" + fileName

        oldFile = open(fileName, "r")
        newFile = open(tempFileName, "w")

        barcodeToRemove = str(barcodeToRemove)

        #cycles through moving all entries from the old file to the new one bar the entry to remove
        for item in oldFile :
            checkItem = Item.Item(self.__FormatFromFile(item))
            if (checkItem.barcode != barcodeToRemove) :
                newFile.write(item)

        oldFile.close()
        newFile.close()

        #removes the old file and renames the new one to the original file name
        os.remove(fileName)
        os.rename(tempFileName, fileName)

    def __AlterNumInStock(self, barcode, numToAdjust) :
        #adjust the amount of stock an item has

        barcode = str(barcode)

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

        #creates a new location file with header
        newStock = open(self.locationFileName, "w")
        newStock.write("Barcode,Location\n")
        newStock.close()
        

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