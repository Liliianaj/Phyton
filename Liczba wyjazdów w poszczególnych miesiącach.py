import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lilianajaskiewicz/Desktop/tabela.csv', sep=';')

print(df.columns)

df['D_wyj'] = pd.to_datetime(df['D_wyj'], format='%Y-%m-%d')

df['Rok_Miesiac'] = df['D_wyj'].dt.to_period('M')

departure_counts_monthly = df.groupby('Rok_Miesiac').size().reset_index(name='Liczba wyjazdów')

plt.figure(figsize=(12, 6))
plt.bar(departure_counts_monthly['Rok_Miesiac'].astype(str), 
        departure_counts_monthly['Liczba wyjazdów'], 
        color=plt.cm.Paired.colors[:len(departure_counts_monthly)])
plt.title('Liczba wyjazdów w poszczególnych miesiącach')
plt.xlabel('Miesiąc')
plt.ylabel('Liczba wyjazdów')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Kod wczytuje dane z pliku CSV, przekształca daty w kolumnie 'D_wyj' na format daty i tworzy nową kolumnę 'Rok_Miesiac', która grupuje dane po miesiącach.
# Następnie grupuje dane według tej nowej kolumny, zliczając liczbę wyjazdów w każdym miesiącu.
# Na końcu generuje wykres słupkowy, który wizualizuje liczbę wyjazdów w poszczególnych miesiącach.