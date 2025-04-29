harga_rumah = 400_000_000
dp_persen = 0.25
pajak_persen = 0.2
jangka_waktu = 5*12

dp = harga_rumah * dp_persen
pajak = harga_rumah * pajak_persen
sisa_harga = harga_rumah - dp
cicilan_per_bulan = sisa_harga / jangka_waktu

hasil = f"""
Bukti Pembayaran Rumah Subsidi Pak Adi
-------------------------------------
Harga Rumah          : Rp {harga_rumah:,.0f}
Uang Muka (25%)      : Rp {dp:,.0f}
Pajak (20%)          : Rp {pajak:,.0f}
Sisa Harga Rumah     : Rp {sisa_harga:,.0f}
Cicilan per Bulan    : Rp {cicilan_per_bulan:,.0f} (selama {jangka_waktu} bulan tanpa bunga)
"""

with open("bukti_pembayaran_pak_adi.txt", "w") as file:
    file.write(hasil)

print("Bukti pembayaran berhasil disimpan ke 'bukti_pembayaran_pak_adi.txt'")