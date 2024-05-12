import pandas as pd
import geopandas as gpd
from opencage.geocoder import OpenCageGeocode
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px




# Pfade zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# CSV-Datei in DataFrame laden
df = pd.read_csv(csv_datei)

# Histogramm einer Spalte erstellen
#plt.hist(df['Profile Name'])
#plt.hist(df['Duration'])

plt.show()


df['Start Time'] = pd.to_datetime(df['Start Time'])

# Nur das Datum extrahieren
df['Start Date'] = df['Start Time'].dt.date
dauer_pro_datum = df.groupby('Start Time')['Duration'].sum().reset_index()

# Die ersten Zeilen des DataFrames anzeigen
print(df.head(10))
print(df.info())
print(df.describe())
print(df['Duration'].describe())






# 'Start Time' in Datumsformat konvertieren
df['Start Time'] = pd.to_datetime(df['Start Time'])

# 'Duration' in Stunden, Minuten und Sekunden aufteilen und als separate Spalten hinzufügen
df[['Hours', 'Minutes', 'Seconds']] = df['Duration'].str.split(':', expand=True).astype(int)

# 'Duration' in Stunden umrechnen
df['Duration_in_hours'] = df['Hours'] + df['Minutes'] / 60 + df['Seconds'] / 3600

# DataFrame nach 'Start Time' gruppieren und die Summe der 'Duration_in_hours' für jeden Tag berechnen
summe_zeit_pro_tag = df.groupby(df['Start Time'].dt.date)['Duration_in_hours'].sum().reset_index()
summe_zeit_pro_tag.rename(columns={'Start Time': 'Datum'}, inplace=True)

# Diagramm erstellen
fig = px.bar(summe_zeit_pro_tag, x='Datum', y='Duration_in_hours',
             title='Summe der Zeit für jeden Tag', labels={'Duration_in_hours': 'Summe der Zeit (Stunden)'})
#fig.show()


# Punktdiagramm erstellen
fig2 = px.scatter(summe_zeit_pro_tag, x='Datum', y='Duration_in_hours',
                 title='Summe der Zeit für jeden Tag', labels={'Duration_in_hours': 'Summe der Zeit (Stunden)'},
                 hover_data=['Duration_in_hours'])
fig2.show()

# Datum für die Summe auswählen
ziel_datum = '2019-07-19'

# DataFrame nach dem Ziel-Datum filtern
ziel_df = df[df['Start Time'] == ziel_datum]

# Summe der 'Wert'-Spalte für das Ziel-Datum berechnen
summe_wert = ziel_df['Duration'].sum()

print(summe_wert)