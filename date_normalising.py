import pandas as pd
import re
import numpy as np

# Load the CSV with memory optimization
df = pd.read_csv('stemma_extra_fields.csv', low_memory=False)

def normalize_date_range(date_str):
    if pd.isna(date_str):
        return np.nan

    date_str = date_str.lower().strip()

    # Match "17th century" with optional modifiers
    century_mod = re.match(r'c?\.?\s*(early|mid|late)?[-\s]*?(\d{1,2})(st|nd|rd|th)? century', date_str)
    if century_mod:
        modifier = century_mod.group(1)
        century = int(century_mod.group(2))
        start = (century - 1) * 100 + 1
        end = century * 100
        if modifier == 'early':
            return start + 25
        elif modifier == 'mid':
            return (start + end) // 2
        elif modifier == 'late':
            return end - 25
        else:
            return (start + end) // 2

    # Match "1600s-30s" style (e.g. "c. 1600s-30s")
    match_abbrev_decade_range = re.match(r'c?\.?\s*(\d{4})s\s*[-–]\s*(\d{2})s', date_str)
    if match_abbrev_decade_range:
        start = int(match_abbrev_decade_range.group(1))
        end = int(match_abbrev_decade_range.group(1)[:2] + match_abbrev_decade_range.group(2))
        return (start + end) // 2

    # Match "1640s-60s"
    match_decade_range = re.match(r'c?\.*\s*(\d{3})(\d)0s[-–](\d{1,2})0s', date_str)
    if match_decade_range:
        base = int(match_decade_range.group(1)) * 10
        start = base + int(match_decade_range.group(2)) * 10
        end = base + int(match_decade_range.group(3)) * 10
        return (start + end) // 2

    # Match "1640s"
    match_decade = re.match(r'c?\.*\s*(\d{4})s', date_str)
    if match_decade:
        year = int(match_decade.group(1))
        return year + 5

    # Match "1600-1630"
    match_range = re.match(r'c?\.*\s*(\d{3,4})\s*[-–]\s*(\d{3,4})', date_str)
    if match_range:
        return (int(match_range.group(1)) + int(match_range.group(2))) // 2

    # Match single 4-digit year
    match_year = re.match(r'.*(\d{4}).*', date_str)
    if match_year:
        return int(match_year.group(1))

    return np.nan




# Apply the normalization
df['normalized_date'] = df['Date Range'].apply(normalize_date_range)

# Sort by Celm No (convert to string just in case of mixed types)
df_sorted = df.sort_values(by='Celm No', key=lambda x: x.astype(str))

# Save the result
df_sorted.to_csv('normalized_stemma_3.1_extra_fields.csv', index=False)

# Preview
print(df_sorted[['Celm No', 'Date Range', 'normalized_date']].head(20))


print(normalize_date_range("c. 1600s-30s"))  # ➜ 1615
