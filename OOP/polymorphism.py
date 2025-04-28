class Burung:
    def suara(self):
        print("Burung berkicau.")

class Anjing:
    def suara(self):
        print("Anjing menggonggong.")

def buat_suara(hewan):
    hewan.suara()

# Penggunaan
burung = Burung()
anjing = Anjing()

buat_suara(burung)  # Output: Burung berkicau.
buat_suara(anjing)  # Output: Anjing menggonggong.