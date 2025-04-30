# Data disimpan dalam struktur sederhana
cart = []

def add_item(cart, item):
    return cart + [item]

def calculate_total(cart):
    return sum(item['price'] for item in cart)

def print_receipt(cart):
    for item in cart:
        print(f"{item['name']}: Rp{item['price']}")
    print(f"Total: Rp{calculate_total(cart)}")

# Contoh penggunaan:
cart = add_item(cart, {'name': 'Sepatu Sneaker', 'price': 20000})
cart = add_item(cart, {'name': 'Sandal', 'price': 5000})
print_receipt(cart)