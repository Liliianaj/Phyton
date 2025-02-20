import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lilianajaskiewicz/Desktop/tabela.csv', sep=';')

print(df.columns)

df['Koszt_wyj'] = df['Koszt_wyj'].str.replace(',', '.').astype(float)

city_costs = df.groupby('Miasto')['Koszt_wyj'].sum().reset_index()

city_costs = city_costs.sort_values(by='Koszt_wyj')

plt.figure(figsize=(12, 6))
plt.bar(city_costs['Miasto'], city_costs['Koszt_wyj'], color=plt.cm.Paired.colors[:len(city_costs)])
plt.title('Łączny koszt wyjazdów w różnych miastach')
plt.xlabel('Miasto')
plt.ylabel('Łączny koszt (zł)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Kod wczytuje dane z pliku CSV, przekształca wartości w kolumnie 'Koszt_wyj', zamieniając przecinki na kropki i konwertując je na liczby zmiennoprzecinkowe.
# Następnie grupuje dane według miast, sumując łączny koszt wyjazdów w każdym z nich.
# Na końcu generuje wykres słupkowy, który przedstawia łączny koszt wyjazdów w różnych miastach, posortowany rosnąco.