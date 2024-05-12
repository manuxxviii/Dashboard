import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
import plotly.express as px
from wordcloud import WordCloud
from sklearn.decomposition import TruncatedSVD

# Pfad zur CSV-Datei
csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'

# DataFrame aus CSV-Datei lesen
df = pd.read_csv(csv_datei)

# Merkmalsvektoren aus den Titeln erstellen
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Title'])


'''
# Liste der Summe der quadratischen Abstände zu den nächsten Zentroiden für verschiedene Anzahlen von Clustern
sum_of_squared_distances = []
K_range = range(1, 11)  # Testen Sie verschiedene Anzahlen von Clustern von 1 bis 10

for k in K_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    sum_of_squared_distances.append(kmeans.inertia_)

# Elbow-Methode: Plot der Summe der quadrierten Abstände zu den nächsten Zentroiden in Abhängigkeit von der Anzahl der Cluster
plt.plot(K_range, sum_of_squared_distances, 'bx-')
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Summe der quadrierten Abstände')
plt.title('Elbow-Methode zur Bestimmung der Anzahl der Cluster')
plt.show()

'''
'''
# KMeans-Modell initialisieren und anpassen
kmeans = KMeans(n_clusters=10)  # Anzahl der Cluster festlegen
kmeans.fit(X)

# Clusteretiketten für jeden Titel erhalten
cluster_labels = kmeans.labels_

# Ergebnisse der Clusteranalyse zum DataFrame hinzufügen
df['Cluster'] = cluster_labels

# Hierarchische Clusteranalyse durchführen und Verknüpfungsmatrix erstellen
linkage_matrix = linkage(X.toarray(), method='ward')

# Dendrogramm anzeigen
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix, labels=df['Title'].values, orientation='right')
plt.xlabel('Distanz')
plt.ylabel('Titel')
plt.title('Hierarchisches Clustering der Titel')
plt.show()
'''
# Liste von Wörtern, die ausgeschlossen werden sollen
#exclude_words = ['the', 'of', 'and', 'in', 'to', 'a', 'bei', 'von', 'staffel', 'folge', 'folgen', 'folgte']
# Funktion zum Filtern der Titel
# Funktion zum Filtern der Titel

# Wörter, die ausgeschlossen werden sollen
exclude_words = ['Staffel', 'Folge', 'staffel', 'folge', 'teil', ' folge ', 'folge ', ' folge']

# Funktion zum Filtern der Sätze
def filter_sentences(sentence):
    words = sentence.lower().split()  # Sätze in Wörter aufteilen und in Kleinbuchstaben konvertieren
    filtered_words = [word for word in words if word not in exclude_words]
    return ' '.join(filtered_words)

# Sätze filtern
df['Filtered_Titles'] = df['Title'].apply(filter_sentences)

# Wordcloud erstellen
text = ' '.join(df['Filtered_Titles'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Wordcloud anzeigen
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

plt.savefig('Wordcloud.png')
plt.show()
