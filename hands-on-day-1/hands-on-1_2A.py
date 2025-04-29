total_cost = 13000000000
down_payment = 0.25 * total_cost
remaining_cost = total_cost - down_payment

try:
    tahun = int(input("Masukkan jangka waktu cicilan (5, 10, 20, 25 tahun): "))
    if tahun not in [5, 10, 20, 25]:
        print("Simulasi tidak tersedia")
    else:
        bulan = tahun * 12
        cicilan_per_bulan = remaining_cost / bulan
        print(f"Cicilan per bulan untuk {tahun} tahun adalah: Rp{cicilan_per_bulan:,.0f}")
except ValueError:
    print("Error: Input harus berupa angka.")