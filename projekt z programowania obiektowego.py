# pracownik.py
class Pracownik(ABC):
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stanowisko = None
        self._wynagrodzenie = None

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

    @abstractmethod
    def oblicz_wynagrodzenie(self):
        pass

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, stanowisko: {self.stanowisko}, wynagrodzenie: {self.wynagrodzenie}"

# programista.py
class Programista(Pracownik):
    def __init__(self, imie, nazwisko, jezyk):
        super().__init__(imie, nazwisko)
        self._jezyk = jezyk

    @property
    def jezyk(self):
        return self._jezyk

    @jezyk.setter
    def jezyk(self, value):
        self._jezyk = value

    def oblicz_wynagrodzenie(self):
        # Logika obliczania wynagrodzenia dla programisty
        return 5000  # Przykładowa wartość

# zarzadzanie_zasobami_ludzkimi.py
class ZarzadzanieZasobamiLudzkimi:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(self, pracownik):
        if isinstance(pracownik, Pracownik):
            self.pracownicy.append(pracownik)
        else:
            raise ValueError("Obiekt musi być instancją klasy Pracownik lub jej pochodnej.")

    def usun_pracownika(self, imie, nazwisko):
        pracownik = next((p for p in self.pracownicy if p.imie == imie and p.nazwisko == nazwisko), None)
        if pracownik:
            self.pracownicy.remove(pracownik)
            print(f"Pracownik {imie} {nazwisko} został usunięty.")
        else:
            print("Pracownik nie został znaleziony.")

    def edytuj_pracownika(self, imie, nazwisko, nowe_imie=None, nowe_nazwisko=None, nowe_stanowisko=None, nowe_wynagrodzenie=None):
        pracownik = next((p for p in self.pracownicy if p.imie == imie and p.nazwisko == nazwisko), None)
        if pracownik:
            pracownik.imie = nowe_imie if nowe_imie else pracownik.imie
            pracownik.nazwisko = nowe_nazwisko if nowe_nazwisko else pracownik.nazwisko
            pracownik.stanowisko = nowe_stanowisko if nowe_stanowisko else pracownik.stanowisko
            pracownik.wynagrodzenie = nowe_wynagrodzenie if nowe_wynagrodzenie else pracownik.wynagrodzenie
            print(f"Pracownik {pracownik.imie} {pracownik.nazwisko} został zaktualizowany.")
        else:
            print("Pracownik nie został znaleziony.")

    def przegladaj_pracownikow(self):
        for pracownik in self.pracownicy:
            print(pracownik)
