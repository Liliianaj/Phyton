#Napisz program, który prosi użytkownika o podanie dwóch liczb całkowitych, a następnie oblicza i wyświetla ich sumę, różnicę, iloczyn i iloraz. Uważaj na dzielenie przez zero!
try:
    liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
    liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
except ValueError:
    print("Wprowadź poprawne liczby całkowite.")
else:
    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    iloczyn = liczba1 * liczba2

    if liczba2 != 0:
        iloraz = liczba1 / liczba2
        print(f"Suma: {suma}")
        print(f"Różnica: {roznica}")
        print(f"Iloczyn: {iloczyn}")
        print(f"Iloraz: {iloraz}")
    else:
        print("Nie można dzielić przez zero.")

