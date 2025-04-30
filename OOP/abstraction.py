from abc import ABC, abstractmethod

# Abstract class
class MetodePembayaran(ABC):
    @abstractmethod
    def autentikasi(self):
        pass

    @abstractmethod
    def bayar(self, jumlah):
        pass

    @abstractmethod
    def konfirmasi(self):
        pass

# Concrete class 1
class KartuKredit(MetodePembayaran):
    def autentikasi(self):
        print("Memverifikasi nomor kartu dan CVV...")

    def bayar(self, jumlah):
        print(f"Membayar Rp{jumlah} dengan kartu kredit.")

    def konfirmasi(self):
        print("Pembayaran dengan kartu kredit berhasil.")

# Concrete class 2
class GoPay(MetodePembayaran):
    def autentikasi(self):
        print("Memverifikasi akun GoPay...")

    def bayar(self, jumlah):
        print(f"Membayar Rp{jumlah} dengan GoPay.")

    def konfirmasi(self):
        print("Saldo GoPay berhasil dipotong.")

# Concrete class 3
class TransferBank(MetodePembayaran):
    def autentikasi(self):
        print("Memverifikasi akun bank dan PIN...")

    def bayar(self, jumlah):
        print(f"Transfer Rp{jumlah} ke rekening tujuan.")

    def konfirmasi(self):
        print("Transfer bank berhasil.")

# Fungsi umum (pakai abstraction)
def proses_pembayaran(metode: MetodePembayaran, jumlah):
    metode.autentikasi()
    metode.bayar(jumlah)
    metode.konfirmasi()

print("=== Pembayaran dengan Kartu Kredit ===")
proses_pembayaran(KartuKredit(), 500000)

print("\n=== Pembayaran dengan GoPay ===")
proses_pembayaran(GoPay(), 150000)

print("\n=== Pembayaran dengan Transfer Bank ===")
proses_pembayaran(TransferBank(), 300000)