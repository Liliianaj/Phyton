from pracownicy import Programista
from zarzadzanie_zasobami_ludzkimi import ZarzadzanieZasobamiLudzkimi

zarzadzanie = ZarzadzanieZasobamiLudzkimi()

pracownik1 = Programista("Jan", "Kowalski", "Python")
pracownik2 = Programista("Anna", "Nowak", "Java")
pracownik3 = Programista("Kasia", "Basia", "C++")
pracownik4 = Programista("Mary", "Chreisler", "JS")

zarzadzanie.dodaj_pracownika(pracownik1)
zarzadzanie.dodaj_pracownika(pracownik2)
zarzadzanie.dodaj_pracownika(pracownik3)
zarzadzanie.dodaj_pracownika(pracownik4)

zarzadzanie.edytuj_pracownika("Jan", "Kowalski", nowe_imie="Janusz", nowe_nazwisko="Kowalczyk")

zarzadzanie.usun_pracownika("Mary", "Chreisler")

zarzadzanie.edytuj_pracownika("Anna", "Nowak", nowe_imie="Basia", nowe_nazwisko="Kasia", nowe_stanowisko="Any", nowe_wynagrodzenie=5000)

zarzadzanie.usun_pracownika("Kasia", "Basia")
