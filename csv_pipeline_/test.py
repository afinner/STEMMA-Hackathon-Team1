import pandas as pd

# Load with low_memory=False to avoid warnings
df = pd.read_csv('stemma_extra_fields.csv', low_memory=False)

# Show the list of columns
print(df.columns.tolist())