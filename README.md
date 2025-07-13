# 📚 Stemma Popularity Analysis

> A project developed during the **Stemma Hackathon** to explore how poetic works circulated and persisted in early modern manuscript culture — by calculating a data-driven **popularity score**.

---

## 🔍 Project Overview

How do we determine which poems were most "popular" in a period without printing presses, publishing contracts, or bestseller lists?

This project uses metadata from poetic manuscripts (especially **CELM numbers**, titles, repositories, and date ranges) to model and score poem popularity across time and archives.

We propose a composite **popularity score** built from three indicators:

- **Frequency**: How often the poem appears (and how many other poems are in that manuscript)
- **Date range span**: How long it circulated (first to last copy)
- **Repository diversity**: How many distinct libraries it appears in

The goal is to **surface which works truly traveled and endured**, and to reflect on what popularity looked like in manuscript culture.

---

## 🧮 Popularity Score Formula
I began by weighting each indicator equally translating it into a score between 0 and 1 by dividing each indicator by the maximum of the indicator:

```text
Popularity Score = (NormFreq + NormSpan + NormRepo) / 3
```
However, I then modified this formula to weight some indicators more as it produced more consistent results:

```text
Popularity Score = 0.5 * NormFreq + 0.3 * NormSpan + 0.2 * NormRepo
```

## Repository Structure
```text
stemma-popularity/
├── csv_pipeline/
│   ├── date_nomalising.py
│   ├── popularity_score.py
│   ├── weighting.py
│   └── repositories.py
│
├── psql_pipeline/
│   ├── query_calculate_popularity.py
│   └── export_scores_sql.py
│
├── results/
├── presentation/
├── requirements.txt
└── README.md
```
---

## Option 1: Using CSV files (requires processing 40 mb through memory)

This guide explains how to generate popularity scores using only the raw CSV files.

---

### 📁 Required Files

From the google drive download:

- `stemma_extra_fields.csv`
- `manuscript_items_07_07_25.csv`

---

### 🐍 Step 1: Set Up the Environment

If you haven’t already:

```bash
# Clone the repository
git clone https://github.com/afinner/STEMMA-Hackathon-Team1.git
cd stemma-popularity

# Install dependencies
pip install -r requirements.txt
```
The full dataset is available as two 40 mb raw csv files:

I don't have permission to share. You could contact [STEMMA](https://stemma.universityofgalway.ie/) to request data?

### 📂 Step 2: Run the CSV Pipeline

Without the reweighted frequency (Update names of csv files):  
1. Run `date_normalising.py`
2. Run `popularity_score.py`
3. Run `repositories.py`
With the reweighted frequency:
1. Just run `weighting.py` (Having problems atm)

## 🗃️ Option 2: Using the SQL File with PostgreSQL

If you prefer to work with a structured SQL database instead of raw CSVs, you can import the full dataset into PostgreSQL using the provided `.sql` dump.

### 🔽 1. Download the SQL file

The full dataset is available as a PostgreSQL-compatible SQL dump:

I don't have permission to share. You could contact [STEMMA](https://stemma.universityofgalway.ie/) to request data?

---

### 🛠️ 2. Set up PostgreSQL

Make sure you have PostgreSQL installed. I downloaded from [postgresql.org](https://www.postgresql.org/):
I used both DBeaver and the VSCode plugin as clients to view data and queries.

Run the python file `query_calculate_popularity.py`
## 🎥 Presentation

- 📊 **Slide deck**  
  _presentation/Popularity_Score_Presentation.pptx_

- 🔁 **Flowchart of algorithm**  
  _presentation/pop_algorithm_flowchart.png_

---

## 🧠 Reflections

This project evolved from several early approaches to organising missing data:

- Lemmatising and matching poem first lines
- Semantic embeddings and cosine similarities
- Using CELM numbers / work_id and structured metadata

Lots of other groups went for the first two ideas and produced nice results

---

## 🌱 Future Directions

- Compare scores to **literary critical reception**
- Correlate popularity with **poetic features** (genre, quality, form)
- Model **temporal decay** or **geographic spread** separately
- Visualize diffusion pathways across time & libraries

---

## 📜 License

MIT License – feel free to use, modify, or build upon this project.

---

## 🙌 Acknowledgements

Thanks to the organizers of the **Stemma Hackathon** ([Stemma](https://stemma.universityofgalway.ie/)), and to all those preserving and cataloguing manuscript poetry and to the [Portershed](https://portershed.com/) for facilitating this event

## TODO
- Finish `weighting.py` for csv
- Build UI with flask for most popular poems




