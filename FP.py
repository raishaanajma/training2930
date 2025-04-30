# PURE FUNCTION: Tidak mengubah data di luar fungsi
def apply_discount(order_total, discount_func):
    return discount_func(order_total)

# FIRST-CLASS & HIGHER-ORDER FUNCTION: Diskon sebagai fungsi
def percentage_discount(percent):
    return lambda total: total * (1 - percent / 100)

def fixed_discount(amount):
    return lambda total: max(0, total - amount)

# RECURSION: Menerapkan banyak diskon secara bertingkat
def apply_discounts_recursive(order_total, discounts):
    if not discounts:
        return order_total
    return apply_discounts_recursive(discounts[0](order_total), discounts[1:])

# Penggunaan:
total = 100000
discounts = [percentage_discount(10), fixed_discount(5000)]
final_total = apply_discounts_recursive(total, discounts)

print(f"Total setelah diskon: Rp{final_total}")