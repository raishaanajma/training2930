from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Meong!")