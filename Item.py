import re

class Item :

    barcode = ""
    name = ""
    price = ""

    def __init__(self, itemDetails = None) :
        #class constructor
        if (itemDetails == None) :
            #acquires input from user if no details are provided
            print("Please input the items details")
            self.SetBarcode()
            self.SetName()
            self.SetPrice()
        elif (len(itemDetails) == 3) :
            #assigns class variables
            self.barcode = itemDetails[0].strip()
            self.name = itemDetails[1].strip()
            self.price = itemDetails[2].strip()

    def PrintItem(self) :
        #display the name and price of the item
        print(self.barcode)
        print(self.name)
        print("Cost : £" + self.price)
    
    def GetDetails(self) :
        #returns a string list of all the items details
        return [self.barcode, self.name, self.price]

    def SetBarcode(self) :
        #takes a barcode input by the user
        _barcode = str(input("Barcode : "))

        #keeps asking for a barcode until a valid barcode is entered
        while (self.__IsBarcodeValid(_barcode) == False) :
            print("Invalid barcode")
            _barcode = str(input("Barcode : "))
        
        #assigns to class variable
        self.barcode = _barcode

    def SetName(self) :
        #takes a name input from the user
        _name = str(input("Name : "))
        self.name = _name

    def SetPrice(self) :
        #takes a prive input from the user
        _price = str(input("Price/£ : "))

        #keeps asking for a price until a valid price is entered
        while (self.__IsPriceValid(_price) == False) :
            print("Invalid price")
            _price = str(input("Price/£ : "))

        #assigns to class variable
        self.price = _price

    def __IsBarcodeValid(self, inputBarcode) :
        #checks the barcode provided is valid
        isValid = False

        #all barcodes are 10 digits long
        if (re.match("\d{10}", inputBarcode)) :
            isValid = True

        return isValid

    def __IsPriceValid(self, inputPrice) :
        #checks the price provided is valid
        isValid = False

        #all prices must have at least two decimal places and be positive
        priceRegEx = "^\d+\.\d\d$"

        if (re.match(priceRegEx, inputPrice)) :
            isValid = True

        return isValid
    
    
