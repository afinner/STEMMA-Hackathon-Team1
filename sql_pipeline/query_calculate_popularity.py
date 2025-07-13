# popularity calculation
# popularity calculation
import psycopg2
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# ---------- Database Connection ----------
def connect_to_db():
    return psycopg2.connect(
        dbname="stemma_db_copy",
        user="postgres",
        password="**********",
        host="localhost",
        port="5432"
    )

# ---------- Query Functions ----------
def fetch_manuscript_items(conn):
    query = """
    SELECT 
        mi.work_id,
        mi.manuscript_id,
        m.repository_id,
        dr.year_start,
        dr.year_end
    FROM manuscript_items mi
    JOIN manuscripts m ON mi.manuscript_id = m.id
    LEFT JOIN date_ranges dr ON mi.date_range_id = dr.id
    WHERE mi.work_id IS NOT NULL
    """
    return pd.read_sql(query, conn)



# ---------- Date Normalization ----------
def compute_normalized_year(df: pd.DataFrame) -> pd.Series:
    """Return the central year as a float: (start + end)/2 or just start if end is null."""
    return df.apply(
        lambda row: (row['year_start'] + row['year_end']) / 2 if pd.notnull(row['year_end']) else row['year_start'],
        axis=1
    )

# ---------- Popularity Score Calculation ----------
def calculate_popularity_scores(df: pd.DataFrame) -> pd.DataFrame:
    df['central_year'] = compute_normalized_year(df)

    # Frequency per work_id
    freq = df.groupby('work_id').size().rename("frequency")

    # Date range span
    span = df.groupby('work_id')['central_year'].agg(
        lambda x: x.max() - x.min() if x.notnull().sum() > 1 else 0
    ).rename("date_range_span")

    # Unique repositories
    repo = df.groupby('work_id')['repository_id'].nunique().rename("unique_repo_count")

    # Reweighted frequency
    manuscript_counts = df.groupby('manuscript_id')['work_id'].count()
    df['manuscript_weight'] = df['manuscript_id'].map(lambda m: 1 / manuscript_counts[m])
    weighted_freq = df.groupby('work_id')['manuscript_weight'].sum().rename("reweighted_frequency")

    # Merge all metrics
    merged = pd.concat([freq, span, repo, weighted_freq], axis=1).reset_index()

    # Normalize metrics
    scaler = MinMaxScaler()
    normed = scaler.fit_transform(merged[['reweighted_frequency', 'date_range_span', 'unique_repo_count']])
    merged[['norm_freq', 'norm_span', 'norm_repo']] = normed

    # Final score
    merged['popularity_score'] = merged[['norm_freq', 'norm_span', 'norm_repo']].mean(axis=1)

    return merged.sort_values(by='popularity_score', ascending=False)

# ---------- Runner Function ----------
def get_top_popular_poems(n: int = 20) -> pd.DataFrame:
    conn = connect_to_db()
    try:
        df = fetch_manuscript_items(conn)
        scored = calculate_popularity_scores(df)
        return scored.head(n)
    finally:
        conn.close()
top_poems = get_top_popular_poems()
print(top_poems)
