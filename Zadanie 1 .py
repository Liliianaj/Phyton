#Napisz program, który oblicza objętość i powierzchnię kuli o zadanym promieniu. Użyj stałej math.pi do reprezentacji liczby pi. Wyświetl wyniki z dokładnością do trzech miejsc po przecinku.
import math

def oblicz_kule(promien):
    objetosc = (4/3) * math.pi * promien**3
    powierzchnia = 4 * math.pi * promien**2
    return objetosc, powierzchnia

promien_kuli = float(input("Podaj promień kuli: "))

objetosc_kuli, powierzchnia_kuli = oblicz_kule(promien_kuli)

print(f"Objętość kuli: {objetosc_kuli}")
print(f"Powierzchnia kuli: {powierzchnia_kuli}")
