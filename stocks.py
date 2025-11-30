class Stocks:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def calculateTotalValue(self):
        return self.quantity * self.price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setPrice(self, price):
        self.price = price

    def updateQuantity(self, amount):
        """Add or subtract from current quantity"""
        self.quantity += amount

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f}/unit"
