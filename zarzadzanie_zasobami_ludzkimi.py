from pracownicy import Pracownik
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
            