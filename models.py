class Product:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {"item_name": self.item_name, "quantity": self.quantity, "price": self.price}

    def __repr__(self):
        return f"{self.item_name}, {self.quantity}, {self.price}"

class Operation:
    def __init__(self, date, operation, item_name, quantity):
        self.date = date
        self.operation = operation
        self.item_name = item_name
        self.quantity = quantity

    def to_dict(self):
        return {"date": self.date, "operation": self.operation, "item_name": self.item_name, "quantity": self.quantity}

    def __repr__(self):
        return f"{self.date}, {self.operation}, {self.item_name}, {self.quantity}"