import pandas as pd

# Load the normalized CSV (or original one if not saved yet)
df = pd.read_csv('normalized_stemma_3_extra_fields.csv', low_memory=False)

# Get unique repository names
unique_repos = df['Repository Name'].dropna().unique()

# Create a mapping from name to ID
repo_id_map = {name: idx for idx, name in enumerate(sorted(unique_repos), start=1)}

# Apply the mapping
df['repository_id'] = df['Repository Name'].map(repo_id_map)

# Save the updated dataset
df.to_csv('stemma_3_with_repository_ids.csv', index=False)

# Optional: Print the mapping for reference
print("Repository ID Mapping:")
for name, idx in repo_id_map.items():
    print(f"{idx}: {name}")

# Preview first few rows
print(df[['Repository Name', 'repository_id']].head(20))
