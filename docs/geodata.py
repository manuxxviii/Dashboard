import pandas as pd
import geopandas as gpd
from opencage.geocoder import OpenCageGeocode
import matplotlib.pyplot as plt

# OpenCage API-Schlüssel
api_key = '7eeabf43876d457eb7e48f9db7ac74f1'

# Geocoder initialisieren
geolocator = OpenCageGeocode(api_key)

# Schritt 1: CSV-Datei einlesen
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/IP_ADDRESSES/IpAddressesStreaming.csv'
df = pd.read_csv(csv_datei)

# Schritt 2: IP-Geolokalisierung mit OpenCage Geocoding API
def geocode_ip(ip):
    try:
        results = geolocator.geocode(ip)
        if results:
            return results[0]['geometry']
        else:
            return None
    except Exception as e:
        print(f"Fehler beim Geocodieren der IP {ip}: {e}")
        return None

df['Coordinates'] = df['Ip'].apply(geocode_ip)

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