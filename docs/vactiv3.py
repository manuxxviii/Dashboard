import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.decomposition import TruncatedSVD

# Annahme: Sie haben bereits eine DataFrame mit Ihren Titeln
# Beispiel-Daten
data = {
    'Title': ['The Matrix', 'The Matrix Reloaded', 'The Matrix Revolutions', 'Inception', 'Interstellar', 'The Dark Knight'],
    # Weitere Merkmale könnten hier sein...
}
df = pd.DataFrame(data)

# Merkmalsvektoren aus den Titeln erstellen
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Title'])

# KMeans-Modell initialisieren und anpassen
kmeans = KMeans(n_clusters=2)  # Anzahl der Cluster festlegen
kmeans.fit(X)

# Clusteretiketten für jeden Titel erhalten
cluster_labels = kmeans.labels_

# Ergebnisse der Clusteranalyse zum DataFrame hinzufügen
df['Cluster'] = cluster_labels

# Merkmalsvektoren aus den Titeln erstellen
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Title'])
linkage_matrix = linkage(X.toarray(), method='ward')

# Ergebnisse anzeigen
print(df)


# Dendrogramm anzeigen
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix, labels=df['Title'].values, orientation='right')
plt.xlabel('Distanz')
plt.ylabel('Titel')
plt.title('Hierarchisches Clustering der Titel')
plt.show()