# 📚 Stemma Popularity Analysis

> A project developed during the **Stemma Hackathon** to explore how poetic works circulated and persisted in early modern manuscript culture — by calculating a data-driven **popularity score**.

---

## 🔍 Project Overview

How do we determine which poems were most "popular" in a period without printing presses, publishing contracts, or bestseller lists?

This project uses metadata from poetic manuscripts (especially **CELM numbers**, titles, repositories, and date ranges) to model and score poem popularity across time and archives.

We propose a composite **popularity score** built from three indicators:

- **Frequency**: How often the poem appears
- **Date range span**: How long it circulated (first to last copy)
- **Repository diversity**: How many distinct libraries it appears in

The goal is to **surface which works truly traveled and endured**, and to reflect on what popularity looked like in manuscript culture.

---

## 🧮 Popularity Score Formula

```text
Popularity Score = (NormFreq + NormSpan + NormRepo) / 3
```

## Repository Structure
```text
stemma-popularity/
├── data/                  # Manuscript metadata and inputs
├── notebooks/             # Jupyter notebooks for analysis and demo
├── scripts/               # Modular Python scripts
├── results/               # Output scores and charts
├── presentation/          # Slides, flowchart, and recordings
├── requirements.txt       # Dependencies
├── LICENSE
└── README.md
```
---

## 🗃️ Optional: Using the SQL File with PostgreSQL

If you prefer to work with a structured SQL database instead of raw CSVs, you can import the full dataset into PostgreSQL using the provided `.sql` dump.

### 🔽 1. Download the SQL file

The full dataset is available as a PostgreSQL-compatible SQL dump:

📥 [Download from Google Drive](https://your-download-link-here)

---

### 🛠️ 2. Set up PostgreSQL

Make sure you have PostgreSQL installed. You can use [Postgres.app](https://postgresapp.com/), Docker, or your system’s package manager:

```bash
# Example (Ubuntu/Debian)
sudo apt install postgresql
```

## 🎥 Presentation

- 📊 **Slide deck**  
  _presentation/Popularity_Score_Presentation.pptx_

- 🔁 **Flowchart of algorithm**  
  _presentation/flowchart.png_

- 📹 _Optional video demo (link if hosted externally)_

---

## 🧠 Reflections

This project evolved from several early approaches:

- ❌ Lemmatising and matching poem first lines
- ❌ Semantic embeddings and cosine distance
- ✅ Using CELM numbers and structured metadata

It reveals both the **possibilities and limits** of computational popularity in literary archives.

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

Thanks to the organizers of the **Stemma Hackathon**, and to all those preserving and cataloguing manuscript poetry — especially the **CELM** project.



