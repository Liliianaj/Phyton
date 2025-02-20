#Napisz program, który generuje losową liczbę z zakresu od 1 do 50, a następnie prosi użytkownika o zgadnięcie tej liczby. Program powinien podpowiadać, czy podana liczba jest za duża, za mała, czy prawidłowa. Użyj modułu random do generowania losowej liczby.
import random

liczba_do_zgadniecia = random.randint(1, 50)

while True:

    zgadnij = int(input("Zgadnij liczbę (od 1 do 50): "))

    if zgadnij == liczba_do_zgadniecia:
        print("Brawo! Zgadłeś!")
        break
    elif zgadnij < liczba_do_zgadniecia:
        print("Za mała liczba. Spróbuj jeszcze raz.")
    else:
        print("Za duża liczba. Spróbuj jeszcze raz.")
