class Dompet:
    def __init__(self):
        self.__uang = 100  # private

    def lihat_uang(self):
        print(f"Uangnya ada {self.__uang}")

dompet = Dompet()
dompet.lihat_uang()  # Bisa lihat
# dompet.__uang  error, karena disembunyiin