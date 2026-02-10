# Protein ID Analysis & Protein Function Exploration

A small bioinformatics project for **exploring protein identifiers and basic dataset structure** and preparing data for **protein function prediction using protein language models (ESM-2)**.

The repository contains Python scripts that:

* read and explore protein IDs from a dataset
* search and filter proteins
* compute statistics
* visualize identifier patterns
* prepare groundwork for downstream protein function prediction workflows

The goal of this project is to demonstrate **data handling, exploratory data analysis (EDA), and computational biology fundamentals** using Python.

---

## 🧬 Project Motivation

Before applying machine learning or protein language models to biological data, we must first **understand the dataset itself**.

In real bioinformatics workflows, poor data quality or hidden biases can completely invalidate a model.
This project focuses on the *very first step* of computational biology pipelines:

> Inspect the biological identifiers before modeling.

Protein IDs (e.g., UniProt accessions) often follow patterns.
By analyzing them we can detect:

* dataset imbalance
* duplicated entries
* identifier family groups
* dataset ordering bias
* data formatting problems

---

## 📂 Project Structure

```
.
├── protein-function-prediction-esm2.py
├── protein_id_plots.py
├── protein_id_advanced_plots.py
└── protein_ids.csv   (user provided dataset)
```

---

## 📊 Dataset

The scripts expect a CSV file containing a column:

```
protein_id
```

Example:

```
protein_id
P12345
Q9XYZ1
A0A024RBG1
```

The program validates the file and will raise an error if the column is missing .

---

## ⚙️ Requirements

Python 3.9+

Install dependencies:

```bash
pip install matplotlib
```

(Standard library modules used: `csv`, `collections`, `statistics`, `pathlib`)

---

## 🔎 1. Protein ID Explorer (Search Tool)

**File:** `protein-function-prediction-esm2.py`

This script loads protein IDs and allows interactive searching.

Features:

* loads protein IDs from CSV
* prints total number of proteins
* displays first 10 entries
* allows prefix search (e.g., P0, Q9)

Example run:

```bash
python protein-function-prediction-esm2.py
```

You will be prompted:

```
Enter a prefix to search (e.g. P0, Q9):
```

The program then shows all matching proteins .

This is useful when investigating:

* protein families
* database origin
* accession numbering patterns

---

## 📈 2. Basic Visual Analysis

**File:** `protein_id_plots.py`

This script performs exploratory data analysis and displays plots:

### Generated visualizations

* Histogram of protein ID length
* First letter frequency bar chart
* Top 20 most common prefixes
* Scatter plot of ID length vs dataset order
* Boxplot of ID length distribution 

Run:

```bash
python protein_id_plots.py
```

---

## 📊 3. Advanced Dataset Analysis

**File:** `protein_id_advanced_plots.py`

A more detailed EDA workflow that **saves images automatically**.

### Outputs

The script generates PNG files:

| Plot                   | Purpose                             |
| ---------------------- | ----------------------------------- |
| Length histogram       | detect identifier formatting issues |
| First letter frequency | database patterns                   |
| Top prefixes           | protein families                    |
| Pie chart              | dominant accession types            |
| Running Q9 fraction    | dataset ordering bias               |

Example:
The running fraction plot checks whether proteins starting with `"Q9"` appear randomly or grouped together .

Run:

```bash
python protein_id_advanced_plots.py
```

Images are saved in the script directory.

---

## 🧠 Why This Matters (Bioinformatics Context)

In protein machine learning:

Bad data → bad embeddings → bad predictions.

Before using deep learning models (like **ESM-2 protein language models**), we must verify:

* distribution consistency
* identifier patterns
* possible sampling bias

For example:
If one protein family dominates the dataset, a neural network will **memorize**, not learn biology.

This project performs a **pre-ML biological sanity check**.

---

## 🔬 Future Work

Planned extensions:

* fetch sequences from UniProt API
* embed sequences with ESM-2
* protein function classification
* GO term prediction
* clustering of protein families

---

## 💻 Skills Demonstrated

This project showcases:

* Python programming
* Data parsing (CSV handling)
* Exploratory Data Analysis (EDA)
* Data visualization (Matplotlib)
* Bioinformatics data preprocessing
* Reproducible scientific workflows

---

## 🚀 How to Use with Your Own Data

1. Create a CSV file:

```
protein_ids.csv
```

2. Add a column:

```
protein_id
```

3. Place it in the same folder as the scripts.

4. Run any script.

---

## 👤 Author

Bioinformatics / IT student portfolio project
Focus areas:

* computational biology
* data science
* machine learning in life sciences

---

## 📜 License

MIT License – free to use for research and educational purposes.
