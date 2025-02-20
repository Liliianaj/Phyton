import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lilianajaskiewicz/Desktop/tabela.csv', sep=';')

print(df.columns)

df['Koszt_wyj'] = df['Koszt_wyj'].str.replace(',', '.').astype(float)

max_payment = df.loc[df.groupby('Miasto')['Koszt_wyj'].idxmax()]

plt.figure(figsize=(12, 6))

bars = plt.bar(max_payment['Miasto'], max_payment['Koszt_wyj'], color=plt.cm.Paired.colors[:len(max_payment)])

plt.title('Osoba, która zapłaciła najwięcej za wyjazd w każdym mieście')
plt.xlabel('Miasto')
plt.ylabel('Koszt wyjazdu (zł)')
plt.xticks(rotation=45)

for i, bar in enumerate(bars):
    label = f"{max_payment.iloc[i]['Imie']} {max_payment.iloc[i]['Nazwisko']}"
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), label,
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.show()

print(max_payment[['Miasto', 'Imie', 'Nazwisko', 'Koszt_wyj']])


# Kod wczytuje dane z pliku CSV, przekształca wartości w kolumnie 'Koszt_wyj', zamieniając przecinki na kropki i konwertując je na liczby zmiennoprzecinkowe.
# Następnie dla każdego miasta znajduje osobę, która zapłaciła najwięcej za wyjazd, a wyniki - wraz z imionami i nazwiskami są wyświetlane na wykresie słupkowym.
