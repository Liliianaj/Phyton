#Napisz program, który sprawdza, czy podana przez użytkownika liczba jest podzielna przez 3. Użyj operatora modulo (%) do sprawdzenia reszty z dzielenia przez 3.
liczba = int(input("Podaj liczbe: "))

if liczba % 3 == 0:
    print("Liczba {} jest podzielna przez 3.".format(liczba))
else:
    print("Liczba {} nie jest podzielna przez 3.".format(liczba))
