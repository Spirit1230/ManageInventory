import Inventory

class StockChecker :

    storeInventory = None

    def __init__(self, inventoryLink) :
        self.storeInventory = Inventory.Inventory(inventoryLink)

    def FindItem(self) :
        self.storeInventory.SearchItem()