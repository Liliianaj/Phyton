import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lilianajaskiewicz/Desktop/tabela.csv', sep=';')

print(df.columns)

df['Koszt_wyj'] = df['Koszt_wyj'].str.replace(',', '.').astype(float)

df['D_wyj'] = pd.to_datetime(df['D_wyj'], format='%Y-%m-%d')

df['Kwartał'] = df['D_wyj'].dt.to_period('Q')

city_departures = df.groupby('Miasto').size().reset_index(name='Liczba_wyjazdów')

top_cities = city_departures.nlargest(3, 'Liczba_wyjazdów')['Miasto']

df_top_cities = df[df['Miasto'].isin(top_cities)]

quarter_city_counts = df_top_cities.groupby(['Kwartał', 'Miasto']).size().reset_index(name='Liczba_wyjazdów')

quarter_city_totals = quarter_city_counts.groupby('Kwartał')['Liczba_wyjazdów'].transform('sum')
quarter_city_counts['Procent'] = (quarter_city_counts['Liczba_wyjazdów'] / quarter_city_totals) * 100

plt.figure(figsize=(10, 6))

colors = plt.cm.Paired.colors[:len(top_cities)]
for idx, city in enumerate(top_cities):
    city_data = quarter_city_counts[quarter_city_counts['Miasto'] == city]
    plt.bar(city_data['Kwartał'].astype(str), 
            city_data['Procent'], 
            label=city, 
            color=colors[idx])

plt.title('Procent wyjazdów w różnych kwartałach dla 3 miast z największą liczbą wyjazdów')
plt.xlabel('Kwartał')
plt.ylabel('Procent wyjazdów (%)')
plt.legend(title="Miasta")
plt.tight_layout()
plt.show()

# Kod wczytuje dane z pliku CSV, przekształca wartości w kolumnie 'Koszt_wyj' na liczby zmiennoprzecinkowe, a daty w kolumnie 'D_wyj' na format daty.
# Następnie tworzy nową kolumnę 'Kwartał', grupuje dane po miastach i wybiera trzy miasta z największą liczbą wyjazdów.
# Dla tych miast oblicza liczbę wyjazdów w poszczególnych kwartałach oraz procentowy udział wyjazdów w każdym kwarcie w odniesieniu do sumy wyjazdów w danym kwartale.
# Na koniec generuje wykres słupkowy, który przedstawia procent wyjazdów w różnych kwartałach dla trzech miast, z różnymi kolorami dla każdego miasta.