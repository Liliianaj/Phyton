#Napisz program, który prosi użytkownika o podanie liczby naturalnej n, a następnie wyświetla n-ty wyraz ciągu arytmetycznego o różnicy 3 i pierwszym wyrazie 1.
def oblicz_wyraz(n):
    pierwszy_wyraz = 1
    roznica = 3
    nty_wyraz = pierwszy_wyraz + (n - 1) * roznica
    return nty_wyraz

try:
    n = int(input("Podaj liczbę naturalną n: "))
    if n <= 0:
        raise ValueError("Podana liczba musi być większa od zera.")
    
    wynik = oblicz_wyraz(n)
    print(f"{n}-ty wyraz ciągu arytmetycznego o różnicy 3 i pierwszym wyrazie 1 to: {wynik}")

except ValueError as x:
    print(f"Błąd: {x}. Podana wartość nie jest liczbą naturalną.")
except Exception as x:
    print(f"Wystąpił błąd: {x}")
