class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cashier:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.cart)

    def print_receipt(self):
        for item in self.cart:
            print(f"{item.name}: Rp{item.price}")
        print(f"Total: Rp{self.calculate_total()}")

# Contoh penggunaan:
kasir = Cashier()
kasir.add_item(Item('Sepatu Sneaker', 20000))
kasir.add_item(Item('Sandal', 5000))
kasir.print_receipt()