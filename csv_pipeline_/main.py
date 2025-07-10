import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from plotly import graph_objs as go
import numpy as np

# Load the first 100 rows of the CSV
df = pd.read_csv('manuscript_items_07_07_25.csv', nrows=100)
print("Data loaded!")

# Choose the column to embed (e.g., 'Title')
texts = df['Title'].fillna('').astype(str).tolist()

# Load a sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Sentence Tranformer Loaded!")
# Compute embeddings
embeddings = model.encode(texts)
print("Embeddings Calculated")

# Prepare hover text for each point
hover_text = [
    f"Title: {row['Title']}<br>Author: {row['Author']}<br>Date: {row['Date Range']}" 
    for _, row in df.iterrows()
]

# Embed 10 Kanye West songs
num_songs = 10
song_texts = songs[:num_songs]
song_embeddings = model.encode(song_texts)

# Combine manuscript and song embeddings
all_embeddings = np.vstack([embeddings, song_embeddings])

# Update hover text to include song info
song_hover_text = [f"Kanye Song {i+1}: {song_texts[i][:40]}..." for i in range(num_songs)]
all_hover_text = hover_text + song_hover_text

# 3D t-SNE
all_tsne_3d = TSNE(n_components=3, random_state=42).fit_transform(all_embeddings)

fig_tsne = go.Figure()
# Manuscript points
fig_tsne.add_trace(go.Scatter3d(
    x=all_tsne_3d[:len(embeddings), 0],
    y=all_tsne_3d[:len(embeddings), 1],
    z=all_tsne_3d[:len(embeddings), 2],
    mode='markers',
    marker=dict(size=6, color='blue', opacity=0.7),
    text=hover_text,
    hoverinfo='text',
    name='Manuscripts',
))
# Song points
fig_tsne.add_trace(go.Scatter3d(
    x=all_tsne_3d[len(embeddings):, 0],
    y=all_tsne_3d[len(embeddings):, 1],
    z=all_tsne_3d[len(embeddings):, 2],
    mode='markers',
    marker=dict(size=8, color='red', opacity=0.9, symbol='diamond'),
    text=song_hover_text,
    hoverinfo='text',
    name='Kanye Songs',
))
fig_tsne.update_layout(title='3D t-SNE of Title Embeddings + Kanye Songs')
fig_tsne.show()

# 3D PCA
all_pca_3d = PCA(n_components=3).fit_transform(all_embeddings)

fig_pca = go.Figure()
fig_pca.add_trace(go.Scatter3d(
    x=all_pca_3d[:len(embeddings), 0],
    y=all_pca_3d[:len(embeddings), 1],
    z=all_pca_3d[:len(embeddings), 2],
    mode='markers',
    marker=dict(size=6, color='green', opacity=0.7),
    text=hover_text,
    hoverinfo='text',
    name='Manuscripts',
))
fig_pca.add_trace(go.Scatter3d(
    x=all_pca_3d[len(embeddings):, 0],
    y=all_pca_3d[len(embeddings):, 1],
    z=all_pca_3d[len(embeddings):, 2],
    mode='markers',
    marker=dict(size=8, color='orange', opacity=0.9, symbol='diamond'),
    text=song_hover_text,
    hoverinfo='text',
    name='Kanye Songs',
))
fig_pca.update_layout(title='3D PCA of Title Embeddings + Kanye Songs')
fig_pca.show()