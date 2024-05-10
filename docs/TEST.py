import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Daten für das Diagramm
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 350]

# Erstellen des Diagramms
plt.plot(x, y)
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Beispiel-Diagramm')


# Speichern des Plots als Bild
plt.savefig('plot1.png')


# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Erstellen des interaktiven Diagramms
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
fig.update_layout(title='Interaktives Diagramm', xaxis_title='X-Achse', yaxis_title='Y-Achse')

# Speichern des Diagramms als HTML-Datei
fig.write_html('plotly_plot.html')