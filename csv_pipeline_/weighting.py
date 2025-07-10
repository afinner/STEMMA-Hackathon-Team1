import pandas as pd
import re

# Load both datasets
df_stemma = pd.read_csv("stemma_extra_fields.csv", low_memory=False)
df_items = pd.read_csv("manuscript_items_07_07_25.csv", low_memory=False)

# Step 1: Merge on shared keys: Title + Shelfmark
df = pd.merge(
    df_stemma,
    df_items[['Title', 'Shelfmark', 'manuscript_id']],
    on=['Title', 'Shelfmark'],
    how='left'
)

# Step 2: Normalize CELM No
def normalize_celm(celm):
    if pd.isna(celm):
        return None
    return re.sub(r'(?i)[\W_]*work[\W_]*', '', str(celm)).strip()

df['normalized_celm'] = df['Celm No'].apply(normalize_celm)

# Step 3: Drop rows missing manuscript or celm info
df = df.dropna(subset=['normalized_celm', 'manuscript_id'])

# Step 4: Count number of items per manuscript
manuscript_counts = df.groupby('manuscript_id')['normalized_celm'].count()

# Step 5: Assign weight = 1 / manuscript poem count
df['manuscript_weight'] = df['manuscript_id'].map(lambda m: 1 / manuscript_counts[m])

# Step 6: Sum weights by poem
reweighted_freq = df.groupby('normalized_celm')['manuscript_weight'].sum().reset_index()
reweighted_freq.rename(columns={'manuscript_weight': 'reweighted_frequency'}, inplace=True)

# Step 7: Sort and export
reweighted_freq_sorted = reweighted_freq.sort_values(by='reweighted_frequency', ascending=False)
reweighted_freq_sorted.to_csv("reweighted_poem_frequencies.csv", index=False)

# Preview
print(reweighted_freq_sorted.head(20))
