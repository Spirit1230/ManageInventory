class Item :

    barcode = ""
    name = ""
    price = ""
    numberInStock = "0"

    def __init__(self, itemDetails = None) :
        if (itemDetails == None) :
            print("Please input the items details")
            self.barcode = str(input("Barcode : "))
            self.name = str(input("Name : "))
            self.price = str(input("Price : "))
            self.numberInStock = "0"
        elif (len(itemDetails) == 4) :
            self.barcode = itemDetails[0]
            self.name = itemDetails[1]
            self.price = itemDetails[2]
            self.numberInStock = itemDetails[3]

    def PrintItem(self) :
        print(self.name)
        print("Cost : £" + self.price)
        print(self.numberInStock + " in stock")
    
    def GetDetails(self) :
        return [self.barcode, self.name, self.price, self.numberInStock]
