# 🌍 World Happiness Report — Data Analysis & Visualization

A complete **Exploratory Data Analysis (EDA)** project using the *World Happiness Report* dataset.
This project analyzes global happiness scores, compares regions, evaluates trends over time, and explores relationships between happiness and socio-economic indicators such as GDP and life expectancy.

It demonstrates practical usage of **Python for Data Analysis**, including data cleaning, statistics, visualization, and trend analysis.

---

## 📊 Example Visualizations

### Happiness Score by Region

![Boxplot](boxplot_region.png)

### Distribution of Happiness Scores

![Histogram](hist_happiness.png)

### Regional Happiness Trends Over Time

![Line Chart](line_regions.png)

---

## 📁 Project Structure

```
World-Happiness-Analysis/
│
├── world_happiness_report.csv     # Dataset
├── world_happiness_analysis.py    # Main analysis script
├── boxplot_region.png             # Regional comparison
├── hist_happiness.png             # Distribution of scores
├── line_regions.png               # Regional trends
└── README.md
```

The main analysis script performs statistical analysis and generates all charts automatically. 

---

## 🧠 Features

### 1. Data Exploration

* Dataset overview
* Descriptive statistics
* Mean, median, min, max, standard deviation
* Country & regional comparisons

### 2. Regional Analysis

* Happiness comparison across world regions
* Regional averages
* Regional trend visualization

### 3. Time-Series Analysis

* Global happiness over multiple years
* Region-based changes over time
* Year-to-year change calculation

### 4. Country Rankings

* Top 10 happiest countries
* Bottom 10 countries
* Country + region information

### 5. Relationship Analysis

* Happiness vs GDP per capita
* Happiness vs life expectancy
* Correlation heatmap
* Regression trendlines

### 6. Additional Metrics

The script computes a new variable:

```
Happiness_Change = Happiness Score (current year) − Happiness Score (previous year)
```

This allows measuring how happiness changes over time for each country. 

---

## 🛠️ Technologies Used

* Python 3
* pandas
* numpy
* matplotlib

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/world-happiness-analysis.git
cd world-happiness-analysis
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib
```

---

## ▶️ How to Run

Run the main program:

```bash
python world_happiness_analysis.py
```

An interactive menu will appear allowing you to choose different analyses and visualizations. 

Example options:

```
1  - Basic statistics
3  - Statistics by region
6  - Happiness histogram
7  - Regional boxplot
8  - Global trend
9  - Regional trends
13 - Correlation heatmap
```

All charts are automatically saved to your Desktop output folder.

---

## 📈 What You Learn From This Project

This project demonstrates practical skills required for:

* Data Analyst roles
* Junior Data Scientist roles
* Python EDA projects
* Visualization portfolio projects

Concepts covered:

* Data cleaning
* GroupBy aggregation
* Statistical summaries
* Correlation analysis
* Regression
* Data visualization
* Time-series analysis

---

## 🎯 Future Improvements

* Interactive dashboards (Plotly / Dash)
* Machine learning prediction model
* Country clustering (K-Means)
* Web dashboard deployment (Streamlit)

---

## 🛡️ License

This project is for **educational and portfolio use**.

---

## 👤 Author

Your Name

GitHub: [https://github.com/yourusername](https://github.com/yourusername)

---

⭐ If you found this project helpful, consider giving it a star!
