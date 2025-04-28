class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan bersuara.")

class Kucing(Hewan):  #mewarisi Hewan
    def suara(self):
        print(f"{self.nama} mengeong.")

#penggunaan
kucing = Kucing("Mimi")
kucing.suara()  #output: Mimi mengeong.