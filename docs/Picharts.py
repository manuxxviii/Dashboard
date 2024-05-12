import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Funktion zur Konvertierung von Sekunden in Stunden, Minuten und Sekunden
def convert_seconds_to_hhmmss(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

# Pfad zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# CSV-Datei laden
df = pd.read_csv(csv_datei)

df[['Datum', 'Uhrzeit']] = df['Start Time'].str.split(' ', expand=True)

df['Datum'] = pd.to_datetime(df['Datum'])
df['Uhrzeit'] = pd.to_datetime(df['Uhrzeit'], format='%H:%M:%S').dt.time
df['Duration'] = pd.to_timedelta(df['Duration'])




# Dauer für jeden Profilnamen aggregieren und in Tage umwandeln
duration_by_name = df.groupby('Profile Name')['Duration'].sum().dt.total_seconds() / (24 * 3600)  # Umrechnung von Sekunden in Tage

# Piechart mit Matplotlib erstellen
plt.figure(figsize=(10, 6))
plt.pie(duration_by_name, labels=duration_by_name.index, autopct='%1.1f%%')
plt.title('Duration by Name')
plt.axis('equal')  # Ensure that pie is drawn as a circle


# HTML-Datei erstellen und das Piechart einbetten
with open('piechart.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Piechart</title>\n</head>\n<body>\n')
    f.write('<img src="piechart.png" alt="Piechart">\n')
    f.write('</body>\n</html>')


plt.savefig('piechart.png')
plt.show()