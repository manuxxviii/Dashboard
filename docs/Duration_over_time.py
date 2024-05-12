import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt

# Pfad zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# CSV-Datei laden
df = pd.read_csv(csv_datei)

df[['Datum', 'Uhrzeit']] = df['Start Time'].str.split(' ', expand=True)

df['Datum'] = pd.to_datetime(df['Datum'])
df['Uhrzeit'] = pd.to_datetime(df['Uhrzeit'], format='%H:%M:%S').dt.time
df['Duration'] = pd.to_timedelta(df['Duration']).dt.total_seconds() / 3600


# Die ersten 10 Zeilen der Rohdaten anzeigen
print(df.head(10))
print(df.dtypes)
df_head = df.head(10)
df_head.to_html('erste_10_zeilen.html', index=False)


# Konvertieren der 'Start Time' in Datumsformat und Extrahieren des Datums
df['Start Date'] = pd.to_datetime(df['Start Time']).dt.date

# Gruppieren nach Profil und Startdatum und Summieren der Dauer
df_grouped = df.groupby(['Profile Name', 'Start Date']).agg({'Duration': 'sum'}).reset_index()

# Funktion zum Erstellen des interaktiven Diagramms

# Funktion zum Erstellen des interaktiven Diagramms
def create_interactive_plot(df):
    fig = px.scatter(df, x='Start Date', y='Duration', color='Profile Name',
                 title='Sum of Duration by Profile Name',
                 labels={'Start Date': 'Date', 'Duration': 'Sum of Duration'})

    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )

    )
    return fig

# Diagramm erstellen
fig = create_interactive_plot(df_grouped)
fig.write_html("interaktives_diagramm.html")
# Diagramm anzeigen
fig.show()