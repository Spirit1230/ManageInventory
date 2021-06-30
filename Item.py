class Item :

    barcode = ""
    name = ""
    price = ""
    numberInStock = 0

    def __init__(self) :
        print("Please input the items details")
        self.barcode = str(input("Barcode : "))
        self.name = str(input("Name : "))
        self.price = str(input("Price : "))
        self.numberInStock = "0"

    def __init__(self, _barcode, _name, _price, _numberInStock) :
        self.barcode = _barcode
        self.name = _name
        self.price = _price
        self.numberInStock = _numberInStock

    def PrintItem(self) :
        print(self.name)
        print("Cost : £" + self.price)
        print(self.numberInStock + " in stock")
    
    def GetDetails(self) :
        return [self.barcode, self.name, self.price, self.numberInStock]
