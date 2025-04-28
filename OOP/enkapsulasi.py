class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  #private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah

akun = BankAccount(1000)
akun.setor(500)
akun.tarik(200)
print(akun.lihat_saldo())  #output: 1300