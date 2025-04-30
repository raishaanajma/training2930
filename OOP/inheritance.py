class Hewan:
    def suara(self):
        print("Aku bersuara!")

class Kucing(Hewan):
    pass

k = Kucing()
k.suara()  # "Aku bersuara!" (warisan dari Hewan)