#Store Management
class Item:
    pay_rate =0.8
    def __init__(self, name: list, price: float, quantity: float):
        # Run validations to the received arguments
        assert price >= 0
        assert quantity >= 0

        # Assignment
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7

print(item1.name)
item1.apply_discount()
print(item1.price)
item2.apply_discount()
print(item2.price)
