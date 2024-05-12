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

# Erstelle das Balkendiagramm für jeden Benutzer und speichere es als HTML
for user in data['Profile Name'].unique():
    user_data = user_titles_count[user_titles_count['Profile Name'] == user]
    fig = px.bar(user_data, x='Title', y='Count', title=f"Gesehene Titel für Benutzer '{user}'")
    fig.update_layout(xaxis_tickangle=-45)

    # Speichere das Diagramm als HTML
    html_output = fig.to_html(full_html=False)

    # Speichere das HTML in eine Datei
    with open(f"{user}_titles_chart.html", "w") as file:
        file.write(html_output)