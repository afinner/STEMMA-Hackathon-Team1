import pandas as pd
import re

# Load both datasets
df_stemma = pd.read_csv("stemma_extra_fields.csv", low_memory=False)
df_items = pd.read_csv("manuscript_items_07_07_25.csv", low_memory=False)

# Step 1: Merge using shared columns (Title + Shelfmark to get Manuscript ID and Work ID)
df = pd.merge(
    df_stemma,
    df_items[['Title', 'Shelfmark', 'Manuscript ID', 'Work ID']],
    on=['Title', 'Shelfmark'],
    how='left'
)


# Step 2: Drop rows missing Work ID or Manuscript ID
df = df.dropna(subset=['Work ID', 'Manuscript ID'])

# Optional: Ensure consistent types (may help with grouping)
df['Work ID'] = df['Work ID'].astype(str)
df['Manuscript ID'] = df['Manuscript ID'].astype(str)

# Step 3: Count how many poems are in each manuscript
manuscript_counts = df.groupby('Manuscript ID')['Work ID'].count()

# Step 4: Assign weight = 1 / manuscript size
df['manuscript_weight'] = df['Manuscript ID'].map(lambda m: 1 / manuscript_counts[m])

# Step 5: Sum weights by Work ID (reweighted frequency)
reweighted_freq = df.groupby('Work ID')['manuscript_weight'].sum().reset_index()
reweighted_freq.rename(columns={'manuscript_weight': 'reweighted_frequency'}, inplace=True)

# Step 6: Sort and save
reweighted_freq_sorted = reweighted_freq.sort_values(by='reweighted_frequency', ascending=False)
reweighted_freq_sorted.to_csv("reweighted_poem_frequencies.csv", index=False)

# Step 7: Preview top results
print(reweighted_freq_sorted.head(20))
