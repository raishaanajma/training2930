total_cost = 13_000_000_000
current_saving = 50_000
annual_salary = 60_000_000 * 0.2

down_payment = 0.25 * total_cost

#A
down_payment_time = down_payment / annual_salary

print("Waktu untuk uang muka:", down_payment_time, "tahun")

#B
growth_rate = 0.035
remaining_cost = total_cost - down_payment
cumulative_saving = 0
payment_years = 0

while cumulative_saving < remaining_cost:
    remaining_cost *= (1 + growth_rate)  # Harga sisa naik tiap tahun
    cumulative_saving += annual_salary
    payment_years += 1

print("Waktu mencicil sampai lunas:", payment_years, "tahun")