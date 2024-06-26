import matplotlib.pyplot as plt
import plotly.graph_objs as go
import csv
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt




# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Erstellen des interaktiven Diagramms
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
fig.update_layout(title='Interaktives Diagramm', xaxis_title='X-Achse', yaxis_title='Y-Achse')

# Speichern des Diagramms als HTML-Datei
fig.write_html('plotly_plot.html')

# Pfad zur CSV-Datei
csv_datei_pfad = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/IP_ADDRESSES/IpAddressesStreaming.csv'

df = pd.read_csv(csv_datei_pfad)




# Schritt 1: CSV-Datei einlesen
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/IP_ADDRESSES/IpAddressesStreaming.csv'
df = pd.read_csv(csv_datei)

# Schritt 2: IP-Geolokalisierung
geolocator = Nominatim(user_agent="geo_locator")
df['Coordinates'] = df['Ip'].apply(geolocator.geocode).apply(lambda x: (x.latitude, x.longitude))

# Extrahiere die Koordinaten in separate Spalten
df[['Latitude', 'Longitude']] = df['Coordinates'].apply(pd.Series)

# Schritt 3: Erstelle ein GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

# Schritt 4: Karte erstellen
# Lade eine Weltkarte
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plotte die Weltkarte
ax = world.plot(figsize=(10, 6), color='white', edgecolor='black')

# Plotte die IP-Adressen
gdf.plot(ax=ax, color='red', marker='o', markersize=5)

# Zeige den Plot an
plt.show()