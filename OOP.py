class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk # atribut objek
        self.warna = warna # atribut objek
        print(self.warna, self.merk)

#Membuat objek dari kelas Mobil
mobil1 = Mobil(merk="Toyota", warna="Merah")