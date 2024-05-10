import matplotlib.pyplot as plt

# Daten für das Diagramm
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Erstellen des Diagramms
plt.plot(x, y)
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Beispiel-Diagramm')


# Speichern des Plots als Bild
plt.savefig('plot.png')
plt.show()