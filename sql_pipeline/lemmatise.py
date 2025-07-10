import spacy
import psycopg2

nlp = spacy.load("en_core_web_sm")

# Connect to PostgreSQL
conn = psycopg2.connect(database="stemma_db_copy", user="postgres", password="andrewroot", host="localhost")
cur = conn.cursor()

# Step 1: Fetch all first lines
cur.execute("SELECT id, first_line FROM manuscript_items;")
rows = cur.fetchall()

# Step 2: Lemmatize and update
for row in rows:
    item_id, first_line = row
    doc = nlp(first_line)
    lemmatized_line = ' '.join([token.lemma_ for token in doc])
    
    cur.execute(
        "UPDATE manuscript_items SET first_line_lemma = %s WHERE id = %s",
        (lemmatized_line.lower().strip(), item_id)
    )

conn.commit()
cur.close()
conn.close()
