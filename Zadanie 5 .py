#Napisz program, który prosi użytkownika o podanie liczby naturalnej n, a następnie wyświetla wszystkie liczby pierwsze mniejsze lub równe n. Liczba pierwsza to taka, która ma dokładnie dwa dzielniki: 1 i siebie samą.
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return False
    return True

n = int(input("Podaj liczbę naturalną n: "))
print("Liczby pierwsze mniejsze lub równe", n, ":")
print([i for i in range(2, n + 1) if czy_pierwsza(i)])



