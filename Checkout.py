import Inventory
import re

class Checkout :

    storeInventory = None
    shoppingList = []
    currentTotalPrice = 0

    def __init__(self, _storeInventoryLink) -> None:
        #class constructor
        self.storeInventory = Inventory.Inventory(_storeInventoryLink) #links checkout to inventory

    def ScanItem(self) :
        #Takes input from the user and adds the specified item to the list
        self.storeInventory.SearchItem()

        #finds exact item in inventory
        itemBarcode = str(input("Please input the barcode of the item to scan : "))
        itemScanned = self.storeInventory.GetItem(itemBarcode)
        numInStock = self.storeInventory.GetStock(itemBarcode)

        if (numInStock == "0") :
            print("Item not available")
        else :
            #adds item to list and increases the total price
            self.shoppingList.append(itemScanned)
            itemPrice = float(itemScanned[2])
            self.currentTotalPrice = self.currentTotalPrice + itemPrice

    def TakePayment(self) :
        payment = str(input("Total cost is " + "{:.2f}".format(self.currentTotalPrice) + "\nPlease input payment : "))

        #continues to ask for payment until alid payment is given
        while (self.__ValidPayment(payment) == False) :
            print("Payment in valid")
            payment = str(input("Please input payment : "))

        #checks if user wants to print the receipt
        wantReceipt = str(input("Thanks for coming\nWould you like a receipt? (y/n) : "))
        if (wantReceipt.lower() == "y") :
            self.__PrintReceipt(payment)

        #removes bought items from the stock inventory
        for item in self.shoppingList :
            itemBarcode = item[0]
            self.storeInventory.RemoveStock(itemBarcode, 1)

    def __PrintReceipt(self, amountPayed) :
        #Takes the items from the list and prints out a receipt
        print()
        print("Item".ljust(30) + "Price /£")
        for item in self.shoppingList :
            name = str(item[1])
            price = str(item[2])
            print(name.ljust(30) + price)
        print()
        print("Total".ljust(30) + "{:.2f}".format(self.currentTotalPrice))  #formats price to 2dp
        print("Amount Payed".ljust(30) + amountPayed)
        print("Change".ljust(30) + "{:.2f}".format(float(amountPayed) - self.currentTotalPrice))    #calculates and diplays change to 2dp
        print()

    def __ValidPayment(self, payment) :
        #checks the payment given is valid
        validPayment = False

        if (re.match("^\d+.\d\d$", payment)) :
            if (float(payment) >= self.currentTotalPrice) :
                validPayment = True

        return validPayment
