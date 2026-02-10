# Protein Dataset Analysis (Bioinformatics Project)

## Project Overview

This project performs exploratory data analysis (EDA) and visualization of a protein dataset using Python.
The goal is to analyze protein sequence properties, detect patterns, and predict protein function using a pretrained deep learning model (ESM-2).

This project demonstrates practical bioinformatics and data analysis skills relevant to research and industry.

---

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Biopython
* Facebook AI Research ESM-2 (protein language model)

---

## Dataset

The dataset contains protein identifiers and sequences stored in:

```
excel_files/protein_ids.csv
```

The data was processed to:

* calculate sequence length
* analyze amino acid frequency
* detect sequence prefixes
* identify patterns in protein structure

---

## Project Structure

```
Protein-Dataset-Analysis/
│
├── excel_files/
│   └── protein_ids.csv
│
├── screenshots/
│   ├── plot1_length_histogram.png
│   ├── plot2_first_letter_frequency.png
│   ├── plot3_top_prefixes.png
│   ├── plot4_first_letter_pie.png
│   └── plot5_running_fraction_Q9.png
│
├── protein_id_plots.py
├── protein_id_advanced_plots.py
└── protein-function-prediction-esm2.py
```

---

## Features

### 1. Protein Length Analysis

* Calculates sequence length
* Visualizes distribution using histograms

### 2. Amino Acid Frequency

* Counts first-letter occurrence
* Generates bar plots and pie charts

### 3. Prefix Pattern Detection

* Finds common sequence prefixes
* Detects potential protein family patterns

### 4. Advanced Visualization

* Running fraction analysis
* Statistical insights

### 5. Protein Function Prediction (Deep Learning)

Uses the ESM-2 protein language model to:

* embed protein sequences
* analyze structural similarity
* assist protein function prediction

---

## Example Output

The project automatically generates plots such as:

* Protein length distribution
* Amino acid frequency
* Prefix occurrence
* Functional pattern trends

(See `/screenshots` folder)

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/Agata-Gabara.git
cd Protein-Dataset-Analysis
```

Install dependencies:

```
pip install pandas numpy matplotlib seaborn biopython torch fair-esm
```

---

## How to Run

Run basic analysis:

```
python protein_id_plots.py
```

Run advanced plots:

```
python protein_id_advanced_plots.py
```

Run protein function prediction:

```
python protein-function-prediction-esm2.py
```

---

## What I Learned

* Bioinformatics data processing
* Protein sequence analysis
* Data visualization
* Using deep learning models in biology
* Working with biological datasets in Python

---

## Author

**Agata Gabara**
IT Graduate | Future Bioinformatician | Data & Python Enthusiast

GitHub: [https://github.com/ag48665](https://github.com/ag48665)
