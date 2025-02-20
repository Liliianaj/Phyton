from abc import ABC, abstractmethod
class Pracownik(ABC):
    def __init__(self, imie, nazwisko, stanowisko, wynagrodzenie):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stanowisko = stanowisko
        self._wynagrodzenie = wynagrodzenie

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, value):
        self._imie = value

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        self._nazwisko = value

    @property
    def stanowisko(self):
        return self._stanowisko

    @stanowisko.setter
    def stanowisko(self, value):
        self._stanowisko = value

    @property
    def wynagrodzenie(self):
        return self._wynagrodzenie

    @wynagrodzenie.setter
    def wynagrodzenie(self, value):
        self._wynagrodzenie = value

    @abstractmethod
    def oblicz_wynagrodzenie(self):
        pass

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, stanowisko: {self.stanowisko}, wynagrodzenie: {self.wynagrodzenie}"



class Programista(Pracownik):
    def __init__(self, imie, nazwisko, jezyk):
        super().__init__(imie, nazwisko, stanowisko="Programista", wynagrodzenie="None")
        self._jezyk = jezyk

    @property
    def jezyk(self):
        return self._jezyk

    @jezyk.setter
    def jezyk(self, value):
        self._jezyk = value

    def oblicz_wynagrodzenie(self):
        return 5000

 


   


