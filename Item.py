import re

class Item :

    barcode = ""
    name = ""
    price = ""

    def __init__(self, itemDetails = None) :
        if (itemDetails == None) :
            print("Please input the items details")
            self.SetBarcode()
            self.SetName()
            self.SetPrice()
        elif (len(itemDetails) == 3) :
            self.barcode = itemDetails[0].strip()
            self.name = itemDetails[1].strip()
            self.price = itemDetails[2].strip()

    def PrintItem(self) :
        print(self.name)
        print("Cost : £" + self.price)
    
    def GetDetails(self) :
        return [self.barcode, self.name, self.price]

    def SetBarcode(self) :
        _barcode = str(input("Barcode : "))

        while (self.__IsBarcodeValid(_barcode) == False) :
            print("Invalid barcode")
            _barcode = str(input("Barcode : "))
        
        self.barcode = _barcode

    def SetName(self) :
        _name = str(input("Name : "))
        self.name = _name

    def SetPrice(self) :
        _price = str(input("Price/£ : "))

        while (self.__IsPriceValid(_price) == False) :
            print("Invalid price")
            _price = str(input("Price/£ : "))

        self.price = _price

    def __IsBarcodeValid(self, inputBarcode) :
        isValid = False

        if (re.match("\d{10}", inputBarcode)) :
            isValid = True

        return isValid

    def __IsPriceValid(self, inputPrice) :
        isValid = False

        priceRegEx = "^\d+\.\d\d$"

        if (re.match(priceRegEx, inputPrice)) :
            isValid = True

        return isValid
    
    
