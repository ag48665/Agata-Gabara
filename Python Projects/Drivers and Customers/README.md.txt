# Drivers and Customers – Data Analysis & Visualization Project

This project provides a complete data analysis workflow for two logistics datasets:

- **customers.csv**
- **drivers.csv**

The Python script `logistics_analysis_desktop.py` :contentReference[oaicite:1]{index=1} loads both datasets, performs descriptive statistics, calculates additional metrics, and generates multiple visualisations. All charts are saved automatically to the user’s Desktop.

---

## 📁 Project Contents

| File | Description |
|------|-------------|
| `customers.csv` | Dataset containing customer attributes, account details, revenue data, freight types, contract dates. |
| `drivers.csv` | Dataset containing driver demographics, experience, employment history, and terminal information. |
| `logistics_analysis_desktop.py` | Full analysis script that generates statistics + visualisations. |

---

# 📊 Key Features of the Analysis

## 1. **Customer Analysis**
The script calculates:

- Annual revenue potential statistics
- Customer distribution by type
- Credit terms distribution
- Account status breakdown
- Freight type distribution
- Contract start year trends

### Customer Visualisations
- Histogram: **Annual Revenue Potential**
- Boxplot: **Revenue by Customer Type**
- Bar chart: **Primary Freight Type**
- Line chart: **New Contracts per Year**

---

## 2. **Driver Analysis**

The script enriches the dataset by computing:

- **Driver age**
- **Tenure length**
- **Experience statistics**
- Employment status distribution
- Home terminal frequency

### Driver Visualisations
- Histogram: **Years of Experience**
- Histogram: **Driver Age**
- Bar chart: **Employment Status**
- Line chart: **Hires per Year**

---

## 3. **Advanced Combined Analysis**

### Correlation Heatmap  
A combined numeric dataset (customer + driver metrics) is generated to detect potential relationships.

Heatmap includes:

- Credit terms  
- Revenue potential  
- Driver age  
- Experience  
- Tenure  

---

# ▶️ How to Run the Project

### Requirements
- Python 3  
- `pandas`  
- `matplotlib`  

Install them with:

```bash
pip install pandas matplotlib
