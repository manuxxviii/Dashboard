import pandas as pd

import matplotlib.pyplot as plt

# Pfad zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# CSV-Datei laden
df = pd.read_csv(csv_datei)

df[['Datum', 'Uhrzeit']] = df['Start Time'].str.split(' ', expand=True)

df['Datum'] = pd.to_datetime(df['Datum'])
df['Uhrzeit'] = pd.to_datetime(df['Uhrzeit'], format='%H:%M:%S').dt.time
df['Duration'] = pd.to_timedelta(df['Duration'])

# Die ersten 10 Zeilen der Rohdaten anzeigen
print(df.head(10))
print(df.dtypes)

df_head = df.head(10)
df_head.to_html('erste_10_zeilen.html', index=False)

# Summe der Dauer berechnen
summe_dauer = df['Duration'].sum()
print("Summe der Dauer:", summe_dauer)

# Statistische Informationen für jede Spalte erhalten
statistiken = df.describe()

# Summe der Dauer zu den statistischen Informationen hinzufügen
statistiken.loc['summe_dauer'] = df['Duration'].sum()
summe_dauer_nach_name = df.groupby('Profile Name')['Duration'].sum()
print(summe_dauer_nach_name)

# HTML-Tabelle der statistischen Informationen erstellen
html_tabelle = statistiken.to_html()


#Duration by name
duration_by_name = df.groupby('Profile Name')['Duration'].apply(lambda x: pd.to_timedelta(x).sum())

# Statistische Informationen für jede Gruppe erhalten
statistics_by_name = df.groupby('Profile Name')['Duration'].describe()

print(statistics_by_name)
html_tabelle2 = statistics_by_name.to_html()

# HTML-Tabelle in eine Datei schreiben
with open('statistiken_namen.html', 'w') as f:
    f.write(html_tabelle2)


# HTML-Tabelle in eine Datei schreiben
with open('statistiken.html', 'w') as f:
    f.write(html_tabelle)


