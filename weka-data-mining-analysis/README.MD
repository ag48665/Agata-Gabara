# WEKA Machine Learning Project — Product Rating Prediction

This project applies **data mining and machine learning techniques** in WEKA to analyse a nutritional dataset and predict product rating categories.

The goal was to move from raw data → patterns → predictive model.

---

## Final Results (Quick Summary)

* Feature selection identified **calories** as the most predictive attribute
* K-Means clustering discovered hidden groups in the dataset
* Logistic Regression and J48 achieved **100% training accuracy**
* Cross-validation accuracy: **~91%**
* Naive Bayes accuracy: **~92%**

The workflow followed a real analytics pipeline: exploration → modelling → evaluation.

---

## Dataset

The dataset contains nutritional information about food products, including:

* calories
* protein
* fat
* sodium
* carbohydrates
* sugars
* vitamins
* rating

The target variable was converted into categories:
**low / medium / high rating** 

---

## Tools Used

* WEKA data mining software
* Statistical analysis
* Clustering algorithms
* Classification algorithms
* Cross-validation testing

---

## Exploratory Data Analysis

### Distribution Analysis

Calories showed a normal distribution:

![Calories Distribution](screenshots/calories-normal-distribution.png)

Protein showed a right-skewed distribution:

![Protein Distribution](screenshots/protein-right-skewed-distribution.png)

Carbohydrates showed a left-skewed distribution:

![Carbohydrates Distribution](screenshots/carbohydrates-left-skewed-distribution.png)

### Class Balance

Understanding rating categories before modelling:

![Class Distribution](screenshots/class-distribution-calories-rating.png)

### Feature Relationship Example

Weak positive relationship between fibre and potassium:

![Fibre vs Potassium](screenshots/fibre-potassium-scatter-plot.png)

---

## Feature Selection

Using **CFS Subset Evaluator + Best First search**, the most useful predictive feature was identified as:

**calories**

![Feature Selection](screenshots/feature-selection-cfs-bestfirst.png)

---

## Unsupervised Learning — Clustering

K-Means clustering grouped the data into two natural clusters (57 instances).

![KMeans Results](screenshots/kmeans-clustering-results.png)

### Cluster Visualization

![Cluster Visualization](screenshots/kmeans-cluster-visualization.png)

### Cluster Centroids Interpretation

Cluster centroids represent average attribute values for each group and help describe the discovered patterns.

![Cluster Centroids](screenshots/kmeans-cluster-centroids.png)

---

## Supervised Learning — Classification Models

Several predictive models were trained:

* Logistic Regression
* J48 Decision Tree
* Simple Logistic
* Naive Bayes

### Logistic Regression

![Logistic Regression](screenshots/logistic-regression-classification-results.png)

### Confusion Matrix

![Confusion Matrix](screenshots/classification-confusion-matrix.png)

### Model Comparison

![Simple Logistic](screenshots/simple-logistic-model-evaluation.png)

### Cross-Validation (Unseen Data)

![Cross Validation](screenshots/multiclass-classification-evaluation.png)

---

## Model Evaluation

Models were evaluated using:

* accuracy
* precision
* recall
* F-measure
* confusion matrix
* 3-fold cross validation

Cross-validation splits the dataset into multiple parts so every data point is tested at least once .

---

## Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Feature selection
* Clustering analysis
* Classification modelling
* Model comparison
* Performance evaluation
* Machine learning workflow

---

## Conclusion

This project demonstrates how structured data can be analysed and transformed into a predictive system.
Both unsupervised and supervised learning approaches were implemented and evaluated, showing that meaningful patterns can be extracted and used to predict rating categories.

---

## Author

**Agata Gabara**
