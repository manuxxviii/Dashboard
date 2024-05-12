import folium
import pandas as pd#
import geopandas as gpd

# CSV-Datei mit den Koordinaten einlesen
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/IP_ADDRESSES/TESTDATEI_coordinates.csv'  # Pfad zur CSV-Datei

csv_dateilaendercodes = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/Ländercodes.csv'
df_laender = pd.read_csv(csv_dateilaendercodes)

weltkarte_pfad = "/Users/mglueck/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
weltkarte = gpd.read_file(weltkarte_pfad)

df = pd.read_csv(csv_datei, skiprows=1, header=None, names=['Zusammengefasst'])

# Karte erstellen
mymap = folium.Map(location=[0, 0], zoom_start=2)  # Startposition und Zoom-Level

# Punkte zur Karte hinzufügen
for index, row in df.iterrows():
    coordinates = row['Zusammengefasst'].split(',')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])
    folium.Marker([latitude, longitude]).add_to(mymap)


# Ländergrenzen zur Karte hinzufügen
for index, row in df_laender.iterrows():
    land = row['CC']
    land_polygon = weltkarte[weltkarte['ADM0_A3'] == land]
    if not land_polygon.empty:
        geo_json = folium.GeoJson(
            land_polygon,
            style_function=lambda feature: {
                'fillColor': 'green',  # Farbe für die Länder
                'color': 'black',      # Farbe für die Grenzen der Länder
                'weight': 1,           # Breite der Ländergrenzen
                'fillOpacity': 1     # Transparenz der Länderfarbe
            }
        )
        geo_json.add_to(mymap)

# Karte anzeigen
mymap.save('map.html')  # Speichern der Karte als HTML-Dateiap.html')  # Speichern der Karte als HTML-Datei