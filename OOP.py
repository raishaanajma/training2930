from abc import ABC, abstractmethod

# ABSTRACTION: Kelas dasar
class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

# INHERITANCE + POLYMORPHISM: Implementasi berbeda
class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent
    
    def apply(self, total):
        return total * (1 - self.percent / 100)

class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, total):
        return max(0, total - self.amount)

# ENCAPSULATION: Diskon dikelola dalam objek
class Order:
    def __init__(self, total):
        self.total = total
        self.discounts = []

    def add_discount(self, discount):
        self.discounts.append(discount)

    def calculate_total(self):
        total = self.total
        for discount in self.discounts:
            total = discount.apply(total)
        return total

# Penggunaan:
order = Order(100000)
order.add_discount(PercentageDiscount(10))
order.add_discount(FixedDiscount(5000))

print(f"Total setelah diskon: Rp{order.calculate_total()}")