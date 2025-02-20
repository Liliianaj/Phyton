#Napisz program, który tworzy listę 5 losowych liczb z zakresu od 1 do 100, a następnie wyświetla średnią tych liczb. Użyj funkcji sum i len do obliczenia średniej.
import random
lista_liczb = [random.randint(1, 100) for i in range(5)]
print("Wylosowane liczby:", lista_liczb)
srednia = sum(lista_liczb) / len(lista_liczb)
print("Średnia liczb:", srednia)
