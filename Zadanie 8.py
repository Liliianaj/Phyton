#Napisz program, który prosi użytkownika o podanie liczby naturalnej n, a następnie sprawdza, czy jest ona liczbą doskonałą. Liczba doskonała to taka, która jest równa sumie swoich dzielników właściwych.

n = int(input("Podaj liczbe naturalna: "))

suma_dzielnikow = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        suma_dzielnikow += i

if suma_dzielnikow == n:
    print("{} to liczba doskonała.".format(n))
else:
    print("{} nie jest liczba doskonałą.".format(n))
