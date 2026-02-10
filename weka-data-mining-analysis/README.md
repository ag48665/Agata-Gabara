
# Data Mining & Machine Learning Analysis (WEKA)

This project presents an end-to-end data mining and machine learning workflow performed using the WEKA data mining toolkit.
The objective was to explore a dataset, identify hidden patterns, and build predictive models capable of classifying product ratings.

The project was completed as part of a Data Management and Business Intelligence module.

---

## Project Objectives
The analysis followed a full Knowledge Discovery in Databases (KDD) process:
1. Understand and explore the dataset
2. Visualize patterns and relationships
3. Discover hidden patterns using unsupervised learning
4. Build classification models using supervised learning
5. Evaluate models using cross-validation
6. Predict unseen data

---

## Dataset Description
The dataset contains nutritional attributes of food products (e.g., cereals).

Attributes include:
- Calories
- Protein
- Fat
- Sodium
- Carbohydrates
- Sugars
- Fibre
- Vitamins
- Cups
- Rating (target variable)

The rating attribute was transformed into a categorical variable rating_bin (Low / Medium / High) for classification.

---

## Exploratory Data Analysis
Several statistical properties were examined:
- Calories: approximately normal distribution
- Protein: right-skewed distribution
- Carbohydrates: left-skewed distribution
- Rating: right-skewed distribution
- Cups: normal distribution

Scatter plot analysis showed mostly weak, positive, non-linear relationships between variables.

---

## Unsupervised Learning

### Association Rules (Apriori)
- Minimum support: 0.1
- Minimum confidence: 0.9
- 8 association rules discovered

### Clustering (K-Means)
- 57 observations
- 2 clusters
- ~65% incorrectly clustered → not reliable for prediction

---

## Feature Selection
Using CFS Subset Evaluator with Best First search, the most important predictive feature identified was:
Calories

---

## Supervised Models

| Model | Accuracy |
|------|------|
| Logistic Regression | 100% |
| Decision Tree (J48) | 100% |
| Simple Logistic | 97.44% |
| Naive Bayes | ~92% |
| 1R | ~90% |

---

## Model Evaluation
3-fold cross validation was used:
- Dataset split into 3 parts
- Each used once for testing and twice for training

The Decision Tree (J48) and Logistic Regression models performed best.

---

## Tools
- WEKA
- Apriori
- K-Means
- Logistic Regression
- Decision Trees
- Naive Bayes

---

## Learning Outcomes
- Data preprocessing
- Exploratory data analysis
- Unsupervised learning
- Supervised machine learning
- Model evaluation

---

## Disclaimer
This project is an academic exercise and not intended for real-world decision-making.
