import matplotlib.pyplot as plt

# Odczyt danych z pliku
num_parts = []
times = []

with open('times_data.txt', 'r') as f:
    # Pomiń nagłówek
    next(f)
    for line in f:
        parts, time = line.strip().split(',')
        num_parts.append(int(parts))
        times.append(float(time))

# Obliczanie wydajności (speedup)
speedup = [times[0] / time for time in times]

# Wykres 1: Zależność czasu przetwarzania od liczby rdzeni
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(num_parts, times, marker='o', linestyle='-', color='b', label='Czas przetwarzania')
plt.title('Czas przetwarzania vs liczba rdzeni')
plt.xlabel('Liczba rdzeni')
plt.ylabel('Czas przetwarzania (s)')
plt.grid(True)
plt.legend()

# Wykres 2: Zależność wydajności (speedup) od liczby rdzeni
plt.subplot(1, 2, 2)
plt.plot(num_parts, speedup, marker='o', linestyle='-', color='r', label='Wydajność (Speedup)')
plt.title('Wydajność (Speedup) vs liczba rdzeni')
plt.xlabel('Liczba rdzeni')
plt.ylabel('Wydajność (Speedup)')
plt.grid(True)
plt.legend()

# Wyświetlenie wykresów
plt.tight_layout()
plt.show()
