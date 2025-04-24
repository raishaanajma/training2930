class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk      # atribut objek
        self.warna = warna    # atribut objek

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

# Membuat objek dari kelas Mobil
mobil1 = Mobil("Toyota", "Merah")
mobil1.info()  # Output: Mobil Toyota berwarna Merah