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
