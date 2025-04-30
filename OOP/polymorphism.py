class Kucing:
    def suara(self):
        print("Meong!")

class Anjing:
    def suara(self):
        print("Guk!")

def hewan_bersuara(hewan):
    hewan.suara()

hewan_bersuara(Kucing())  # Meong!
hewan_bersuara(Anjing())  # Guk!