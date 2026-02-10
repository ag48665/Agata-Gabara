# Airline Customer Satisfaction Analysis (Tableau)

## 📊 Dashboard Preview

Interactive Tableau dashboard combining operational performance metrics and customer satisfaction insights.

![Tableau Dashboard](screenshots/tableau-dashboard-overview.png)

---

## 📊 Project Overview

This project presents an end-to-end data analysis and visualization of airline passenger satisfaction using **Tableau**.

The goal of the project was to analyze customer feedback and flight operational data in order to identify:

* factors influencing passenger satisfaction
* patterns in flight delays
* differences between travel classes
* customer behavior trends

The dataset contains passenger information, service ratings, travel class, delays and flight distance.

---

## 🧠 Business Problem

Airlines collect large amounts of customer data, but without proper analysis they cannot clearly understand:

* Why some passengers are dissatisfied
* Which service areas need improvement
* How delays impact customer experience
* Which customer segments are most valuable

This project simulates a real Business Intelligence scenario where an airline wants to improve customer retention and service quality.

---

## 🗂 Dataset

**Source:** Kaggle – Airline Customer Satisfaction dataset

The dataset includes:

* customer demographics
* travel type (business / personal)
* service ratings (seat comfort, food and drink, online boarding, etc.)
* flight distance
* departure and arrival delays

---

## 🧹 Data Preparation

Before visualization, the dataset required preprocessing:

* removed incomplete records
* handled missing values
* reduced dataset size for analysis
* transformed categorical ratings (0–5) into descriptive labels
* selected relevant analytical features

---

## 📈 Tableau Visualizations

The dashboard contains multiple analytical views:

1. Gender distribution of passengers
2. Departure delay by travel class and travel type
3. Flight distance by customer type and gender
4. Satisfaction comparison by class (Eco, Eco Plus, Business)
5. Departure delay vs arrival delay correlation
6. Flight distance vs delay by age group
7. Passenger age distribution
8. Combined delay analysis

---

## 🖼 Visualization Examples

### Gender Distribution

![Gender Distribution](screenshots/gender-distribution-pie-chart.png)

### Passenger Age Distribution

![Age Distribution](screenshots/age-distribution-histogram-by-gender.png)

### Customer Satisfaction by Class

![Customer Satisfaction](screenshots/customer-satisfaction-treemap-by-class.png)

### Departure Delay by Class and Travel Type

![Departure Delay](screenshots/departure-delay-by-class-and-travel-type.png)

### Flight Distance by Customer Type and Gender

![Flight Distance](screenshots/flight-distance-by-customer-type-and-gender.png)

### Departure vs Arrival Delay Correlation

![Delay Correlation](screenshots/departure-vs-arrival-delay-correlation.png)

### Flight Distance vs Arrival Delay by Age

![Age Analysis](screenshots/flight-distance-vs-arrival-delay-by-age.png)

---

## 🔍 Key Insights

Main findings:

* Business class passengers show the highest satisfaction levels
* Longer delays are associated with lower customer satisfaction
* Loyal customers tend to travel longer distances
* Departure delay strongly predicts arrival delay
* Customer demographics influence travel behavior patterns

---

## 🧰 Tools Used

* Tableau (Data visualization, dashboard development, KPI analysis)
* Excel (Data cleaning & transformation)
* Exploratory Data Analysis (EDA)
* Data storytelling

---

## 📁 Repository Structure

```
/data          → dataset
/dashboard     → Tableau workbook (.twbx)
/screenshots   → dashboard images
README.md      → project documentation
```

---

## 🚀 How to View the Project

1. Download the `.twbx` Tableau file
2. Open using **Tableau Public** or **Tableau Desktop**
3. Explore the interactive dashboard

---

## 💼 Skills Demonstrated

* Data cleaning
* Data transformation
* Exploratory Data Analysis (EDA)
* Data visualization
* Dashboard design
* KPI and operational analysis
* Business Intelligence thinking

---

## 📌 Author

Agata Gabara
Bachelor's Degree in Information Technology

This project is part of my data analytics & business intelligence portfolio.
