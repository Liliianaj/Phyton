#Napisz program, który prosi użytkownika o podanie dowolnego tekstu, a następnie zlicza i wyświetla liczbę liter i cyfr w tym tekście. Użyj funkcji isalpha i isdigit do sprawdzenia, czy dany znak jest literą czy cyfrą.
tekst = input("Podaj dowolny tekst: ")

licznik_liter = 0
licznik_cyfr = 0

for znak in tekst:
    if znak.isalpha():
        licznik_liter += 1
    elif znak.isdigit():
        licznik_cyfr += 1

print("Liczba liter: {}".format(licznik_liter))
print("Liczba cyfr: {}".format(licznik_cyfr))
