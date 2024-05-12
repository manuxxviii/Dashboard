import pandas as pd
import plotly.express as px

# Pfad zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# CSV-Datei laden
data = pd.read_csv(csv_datei)

# Funktion zur Konvertierung der Zeitdauer von HH:MM:SS in Sekunden
def duration_to_seconds(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

# Konvertiere die Dauer-Spalte in Sekunden
data['Duration_Seconds'] = data['Duration'].apply(duration_to_seconds)

# Gruppiere die Daten nach Benutzer und Titel und berechne die Anzahl der gesehenen Titel für jeden Benutzer
user_titles_count = data.groupby(['Profile Name', 'Title']).size().reset_index(name='Count')

# Sortiere die Daten nach der Häufigkeit der gesehenen Titel absteigend
user_titles_count_sorted = user_titles_count.sort_values(by='Count', ascending=False)

# Erstelle das Balkendiagramm für alle Benutzer
fig = px.bar(user_titles_count_sorted, y='Count', x='Title', color='Profile Name')
fig.update_layout(xaxis_tickangle=-90,width=1200, height=1200)
fig.show()

fig.write_html('titel_user_overall.html')

