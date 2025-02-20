import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/lilianajaskiewicz/Desktop/tabela.csv', sep=';')

print(df.columns)

df['D_wyj'] = pd.to_datetime(df['D_wyj'], format='%Y-%m-%d')

df['Kwartał'] = df['D_wyj'].dt.to_period('Q')

departure_counts = df.groupby('Kwartał').size().reset_index(name='Liczba wyjazdów')

plt.figure(figsize=(8, 8))
plt.pie(departure_counts['Liczba wyjazdów'], 
        labels=departure_counts['Kwartał'].astype(str),
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors)  
plt.title('Liczba wyjazdów w zależności od kwartału')
plt.axis('equal')  
plt.tight_layout()  
plt.show()


# Kod wczytuje dane z pliku CSV, przekształca daty w kolumnie 'D_wyj' na format daty i tworzy nową kolumnę 'Kwartał', grupując dane według kwartałów. 
# Następnie grupuje dane po kwartałach, zliczając liczbę wyjazdów w każdym kwartele.
# Na końcu generuje wykres kołowy, który pokazuje procentowy udział wyjazdów w poszczególnych kwartałach.








