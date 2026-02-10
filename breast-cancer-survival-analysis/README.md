# Exploratory Survival Analysis of Breast Cancer Patients (METABRIC) — Power BI

This repository contains an **interactive exploratory survival analysis** of breast cancer patients using the publicly available **METABRIC** dataset, built in **Power BI**. The work demonstrates clinical data preprocessing, time-to-event endpoint definition, and Kaplan–Meier–style survival visualization.

## Project overview

**Goal:** Explore overall survival (OS) and relapse-free survival (RFS) patterns and compare survival trends across clinically meaningful strata (e.g., **ER status**, **Pam50 molecular subtype**).

**What’s included:**
- Data cleaning and feature engineering in **Power Query**
- Survival endpoint creation (event indicators, censoring logic)
- Dynamic measures in **DAX** for:
  - Median OS and median RFS
  - Risk-set–based KM-style survival probability calculation
- Interactive visuals, including a Kaplan–Meier–style OS curve stratified by ER status

## Dataset

- **Source:** METABRIC breast cancer cohort (via Kaggle notebook link in the report)
- **Sample size:** ~2,500 patients
- **Key fields used:**
  - Overall Survival (months)
  - Relapse-Free Survival (months)
  - Survival status (Living / Deceased)
  - ER status
  - Pam50 subtype
  - Treatment/pathological features

> Note: Please respect the dataset’s original license/terms of use when redistributing any data.

## Data preparation (Power Query)

Main preparation steps:
- Convert time-to-event columns to numeric
- Create binary event indicators:
  - `OS_Event` (1 = death, 0 = censored)
  - `RFS_Event` (1 = relapse, 0 = censored)
- Handle missing values with clinically appropriate censoring logic
- Validate internal consistency prior to analysis

## Survival analysis

### Median survival estimates
- **Median Overall Survival (OS)**
- **Median Relapse-Free Survival (RFS)**  
These are computed dynamically and update with report filters/slicers.

### Kaplan–Meier–style survival curve (OS)
A KM-style curve is implemented using:
- Discrete monthly time bins
- Risk-set–based estimation logic
- Censoring-aware survival probability calculation

#### ER-status comparison (example)
The Kaplan–Meier plot suggests **no meaningful difference** in overall survival between **ER-positive** and **ER-negative** groups in this dataset (as shown in the report).

![Kaplan–Meier (OS) by ER Status](KM%20Survival.jpg)

## Tools & skills demonstrated
- Survival analysis concepts (time-to-event, censoring, risk set)
- Power Query (ETL) and data validation
- DAX measures for analytical logic
- Interactive data visualization in Power BI
- Translating biomedical questions into analytic workflows

## Files
- `report.pdf` — short project write-up / narrative
- `KM Survival.jpg` — screenshot of the KM-style OS curve stratified by ER status

## How to view
1. Open the Power BI report file (if included in your version of the repo).
2. Use slicers/filters to stratify by ER status or Pam50 subtype.
3. Inspect median survival measures and the KM-style curves as filters change.

## Disclaimer
This is an **exploratory** analysis for learning/demonstration purposes and is **not** intended for clinical decision-making.
