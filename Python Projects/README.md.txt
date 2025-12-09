🌍 World Happiness Report – Data Analysis & Visualization Project

This project provides a complete exploratory data analysis workflow for the World Happiness Report dataset:

world_happiness_report.csv

The Python script world_happiness_analysis.py loads the dataset, performs descriptive statistics, computes additional metrics (such as year-to-year changes), and generates multiple visualisations.
All charts are saved automatically into a designated Desktop directory.

📁 Project Contents
File	Description
world_happiness_report.csv	Dataset containing country happiness scores, GDP per capita, life expectancy, region data, and socio-economic indicators.
world_happiness_analysis.py	Full analysis script that performs statistics and generates visualisations.

1. Global Happiness Analysis

The script includes:

Basic dataset overview
Summary statistics (mean, median, min, max, standard deviation)
Happiness score distribution
Year-to-year global trends
Region-level comparisons
Top/bottom happiest countries for any selected year
Visualisations Included
Histogram: Happiness Score Distribution
Boxplot: Happiness Scores by Region
Line Chart: Global Average Happiness Across Years
Line Chart: Regional Happiness Trends

2. Country-Level Rankings

For any selected year, the script displays:

Top 10 happiest countries
Bottom 10 countries
Country, region, and happiness score

Visualisations Included
Horizontal Bar Chart: Top 10 Happiest Countries
Horizontal Bar Chart: Bottom 10 Countries

3. Year-to-Year Change Analysis

The dataset is enhanced by computing:
Happiness_Change (difference from the previous year for each country)

Statistics include:
Mean and median change
Distribution of increases/decreases
Visualisation Included
Histogram: Year-to-Year Happiness Score Changes

4. Correlation & Regression Analysis

To explore potential factors influencing happiness, the script generates:

A correlation matrix of all numeric fields
Regression trendlines for key predictors
Visualisations Included
Correlation Heatmap
Scatter Plot: Happiness vs GDP per Capita
Scatter Plot: Happiness vs Life Expectancy

▶️ How to Run the Project
Requirements

Python 3
pandas
numpy
matplotlib

Install dependencies:
pip install pandas numpy matplotlib

Run the Script
python world_happiness_analysis.py


An interactive menu will appear, allowing you to choose different types of analysis and visualisations.

🛡️ License
This project is intended for educational and analytical use.