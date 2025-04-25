import rapihin

rapihin.header(1, "Object Oriented Programming")
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk      #atribut objek
        self.warna = warna    #atribut objek

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

#membuat objek dari kelas Mobil
mobil1 = Mobil("Toyota", "Merah")
mobil1.info()  #output: Mobil Toyota berwarna Merah

rapihin.divider()


rapihin.header(2, "Class Variable vs Instance Variable")
class Kucing:
    spesies = "Oren Gendut"
    def __init__(self,nama):
        self.nama = nama

kucing1 = Kucing("Rehan")
kucing2 = Kucing("Alvan")
print(kucing1.nama)
print(kucing2.nama)

rapihin.divider()