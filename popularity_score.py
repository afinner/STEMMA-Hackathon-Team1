import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load your processed dataset
df = pd.read_csv('stemma_3_with_repository_ids.csv', low_memory=False)

# Total RaW-work-10 entries
print(df[df['Celm No'] == 'RaW-work-10'].shape[0])

# How many remain after dropna()
filtered_df = df.dropna(subset=['Celm No', 'normalized_date', 'repository_id'])
print(filtered_df[filtered_df['Celm No'] == 'RaW-work-10'].shape[0])
# Drop rows with missing required data
df = df.dropna(subset=['Celm No'])  # Only ensure celm is present

date_range_span=('normalized_date', lambda x: x.dropna().max() - x.dropna().min() if x.notna().sum() > 1 else 0)
unique_repo_count=('repository_id', lambda x: x.dropna().nunique())


# Normalize Celm No: extract just the digits (e.g. from "Work 123" or "Poems-Work-123")
df['normalized_celm'] = df['Celm No'].str.replace(r'(?i)-?work-?', '', regex=True)



# Group by normalized_celm
grouped = df.groupby('normalized_celm').agg(
    frequency=('normalized_celm', 'count'),
    date_range_span=('normalized_date', lambda x: x.max() - x.min()),
    unique_repo_count=('repository_id', pd.Series.nunique)
).reset_index()

# Normalize the three indicators using Min-Max scaling
scaler = MinMaxScaler()
normalized = scaler.fit_transform(grouped[['frequency', 'date_range_span', 'unique_repo_count']])
grouped[['norm_freq', 'norm_span', 'norm_repo']] = normalized

# Compute popularity score as the average of normalized indicators
grouped['popularity_score'] = grouped[['norm_freq', 'norm_span', 'norm_repo']].mean(axis=1)

# Optional: sort by popularity
grouped_sorted = grouped.sort_values(by='popularity_score', ascending=False)

# Save the full output
grouped_sorted.to_csv('celm_popularity_scores_detailed_1.csv', index=False)

# Show preview with all components (fix: use normalized_celm instead of 'Celm No')
print(grouped_sorted[['normalized_celm', 'frequency', 'date_range_span', 'unique_repo_count',
                      'norm_freq', 'norm_span', 'norm_repo', 'popularity_score']].head(20))

# Show their corresponding normalized_celm
subset = df[df['Celm No'].str.contains('RaW.*10', na=False)]
print(subset[['Celm No', 'normalized_celm']].drop_duplicates())




