# Promoter vs Non-Promoter Sequence Analysis
This project performs an exploratory bioinformatics analysis of a labeled DNA sequence
dataset to identify features that distinguish promoter (+) from non-promoter (−) regions.

## Project Overview
The analysis focuses on:
- DNA sequence length
- GC content
- Trinucleotide (3-mer) frequency analysis

Promoter and non-promoter sequences are compared to identify characteristic
sequence patterns using simple, interpretable methods.

## Dataset
The dataset consists of fixed-length DNA sequences from *Escherichia coli*.
Each record contains:
- a class label (+ promoter / − non-promoter)
- a sequence identifier
- a nucleotide sequence (A, C, G, T)
The dataset is publicly available on Kaggle.

## Repository Structure
promoter-sequence-analysis/
├── notebooks/ # Jupyter notebook with full analysis
├── figures/ # Generated plots
├── report/ # PDF report with interpretations
├── data/ # Input dataset (optional)
├── requirements.txt
└── README.md


## How to Run

1. Create a virtual environment (optional but recommended)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3.Open the notebook:
jupyter notebook notebooks/promoter_analysis.ipynb

Results
•	Promoter sequences show strong AT-rich 3-mer patterns (AAA, TTT, TTA)
•	Non-promoter sequences exhibit more GC-mixed and coding-like motifs (ATG, TGA, ACG)
•	These differences suggest short k-mer patterns can help discriminate promoter regions
Author
Agata Gabara


