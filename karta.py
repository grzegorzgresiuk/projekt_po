from abc import ABC, abstractmethod

class Karta(ABC):
    def __init__(self, nr_karty, CVV):
        self.__nr_karty = nr_karty
        self.__CVV = CVV

    @abstractmethod
    def getRodzaj(self):
        pass


class KartaKredytowa(Karta):
    def __init__(self, nr_karty, CVV, limit):
        super().__init__(nr_karty, CVV)
        self.__limit = limit

    def getRodzaj(self):
        return "kredytowa"

    def getLimit(self):
        return self.__limit


class KartaDebetowa(Karta):
    def __init__(self, nr_karty, CVV):
        super().__init__(nr_karty, CVV)

    def getRodzaj(self):
        return "kredytowa"


class KartaBankomatowa(Karta):
    def __init__(self, nr_karty, CVV):
        super().__init__(nr_karty, CVV)

    def getRodzaj(self):
        return "kredytowa"
