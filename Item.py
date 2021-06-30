import re

class Item :

    barcode = ""
    name = ""
    price = ""
    numberInStock = "0"

    

    def __init__(self, itemDetails = None) :
        if (itemDetails == None) :
            print("Please input the items details")
            self.barcode = self.__SetBarcode()
            self.name = self.__SetName()
            self.price = self.__SetPrice()
            self.numberInStock = "0"
        elif (len(itemDetails) == 4) :
            self.barcode = itemDetails[0].strip()
            self.name = itemDetails[1].strip()
            self.price = itemDetails[2].strip()
            self.numberInStock = itemDetails[3].strip()

    def PrintItem(self) :
        print(self.name)
        print("Cost : £" + self.price)
        print(self.numberInStock + " in stock")
    
    def GetDetails(self) :
        return [self.barcode, self.name, self.price, self.numberInStock]

    def __SetBarcode(self) :
        return str(input("Barcode : "))

    def __SetName(self) :
        return str(input("Name : "))

    def __SetPrice(self) :
        _price = str(input("Price/£ : "))

        while (self.__IsPriceValid(_price) == False) :
            print("Invalid price")
            _price = str(input("Price/£ : "))

        return _price

    def __IsPriceValid(self, inputPrice) :
        isValid = False

        priceRegEx = "^\d+\.\d\d$"

        if (re.match(priceRegEx, inputPrice)) :
            isValid = True

        return isValid
