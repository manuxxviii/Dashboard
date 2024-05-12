import pandas as pd

# CSV-Datei laden
csv_datei = '/Users/mglueck/PycharmProjects/Dashboard/docs/coordinates.csv'

df = pd.read_csv(csv_datei, header=None, names=['IP Address', 'Latitude', 'Longitude'])

# Zweite und dritte Spalte zusammenfassen, getrennt durch ":"
df['Zusammengefasst'] = df['Latitude'].astype(str) + ',' + df['Longitude'].astype(str)

# Ausgabe des DataFrames
print(df)

df.to_csv('ausgabe.csv', index=False)