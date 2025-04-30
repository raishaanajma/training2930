class Mobil:
    def __init__(self):
        self.__kecepatan = 100  # atribut privat

    def set_kecepatan(self, nilai):
        if nilai >= 0:
            self.__kecepatan = nilai
        else:
            print("Kecepatan tidak boleh negatif!")

    def get_kecepatan(self):
        return self.__kecepatan

m = Mobil()
print(m.get_kecepatan())   # 100
m.set_kecepatan(-50)       # Ditolak!
print(m.get_kecepatan())   # Masih 100