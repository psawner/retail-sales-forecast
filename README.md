# Retail Sales Forecasting & Business Performance Analysis

> An end-to-end Retail Sales Forecasting and Business Analytics project built using Python, Machine Learning, SHAP Explainability, and Power BI to help optimize inventory planning, promotional strategies, and business decision-making.

---

## Project Overview

Retail businesses often struggle to accurately forecast future sales, leading to inventory shortages, excess stock, and inefficient promotional planning.

This project analyzes historical sales data from Rossmann stores and develops an end-to-end forecasting system that predicts future daily sales while providing actionable business insights through interactive dashboards and explainable AI.

The solution combines data analytics, feature engineering, machine learning, model explainability, and business intelligence to simulate a real-world retail forecasting system.

---

## Business Objectives

- Forecast future daily sales for each store
- Identify key drivers influencing sales
- Evaluate the effectiveness of promotional campaigns
- Analyze seasonal sales patterns
- Support inventory planning and resource allocation
- Deliver business insights through interactive Power BI dashboards

---

## Dataset

**Source:** Rossmann Store Sales Dataset (Kaggle)

The project uses the following datasets:

- **train.csv** – Historical daily sales transactions
- **store.csv** – Store metadata
- **test.csv** – Future dates for prediction
- **sample_submission.csv** – Kaggle reference file

---

# Project Workflow

```
Business Understanding
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Model Building
        ↓
Hyperparameter Tuning
        ↓
Model Explainability (SHAP)
        ↓
Business Recommendations
        ↓
Power BI Dashboard
```

---

# Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Joblib

### Visualization

- Power BI

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# Project Structure

```
Retail-Demand-Forecasting/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Business_Understanding.ipynb
│   ├── 02_Data_Loading.ipynb
│   ├── 03_Data_Cleaning.ipynb
│   ├── 04_EDA.ipynb
│   ├── 05_Feature_Engineering.ipynb
│   ├── 06_Model_Building.ipynb
│   └── 07_Business_Insights.ipynb
│
│
├── dashboard/
│
├── reports/
│
├── models/
│
├── images/
│
├── requirements.txt
│
└── README.md
```

---

# Data Analysis

Performed extensive exploratory analysis to understand business performance.

### Key Analysis

- Daily and monthly sales trends
- Top and bottom performing stores
- Promotion effectiveness
- Store type comparison
- Assortment analysis
- Holiday impact
- Competition analysis
- Correlation analysis
- Seasonal patterns

---

# Feature Engineering

Created advanced forecasting features including:

### Calendar Features

- Year
- Month
- Quarter
- Week
- Day
- Day of Year
- Month Start
- Month End
- Weekend Indicator

### Time-Series Features

- Lag 1
- Lag 7
- Lag 14
- Lag 30

### Rolling Statistics

- 7-Day Rolling Mean
- 14-Day Rolling Mean
- 30-Day Rolling Mean
- Rolling Standard Deviation

### Business Features

- Competition Age
- Promotion Duration

### Cyclical Encoding

- Month (Sin/Cos)
- Day of Week (Sin/Cos)

---

# Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

Hyperparameter tuning was performed using **RandomizedSearchCV** to optimize the final XGBoost model.

---

# Model Performance

| Model | MAE | RMSE | R² |
|------|------:|------:|------:|
| Linear Regression | 858.50 | 1214.24 | 0.8511 |
| Decision Tree | 775.23 | 33.35 | 0.8751 |
| Random Forest | 712.19 | 31.90 | 0.8954 |
| **XGBoost** | **629.67** | **29.71** | **0.9213** |

**Final Selected Model:** XGBoost Regressor

---

# Explainable AI

To improve model transparency, SHAP (SHapley Additive Explanations) was used.

Generated explainability visualizations include:

- SHAP Summary Plot
- SHAP Feature Importance
- SHAP Waterfall Plot

These explain how different features influence sales predictions both globally and for individual predictions.

---

# Power BI Dashboard

Developed an interactive executive dashboard consisting of four pages:

### Executive Overview

- Total Sales
- Average Sales
- Total Stores
- Monthly Sales Trend

### Store Performance

- Top 10 Stores
- Bottom 10 Stores
- Revenue by Store Type
- Revenue by Assortment

### Promotion Analysis

- Promotion vs Non-Promotion Sales
- Promotion Impact by Store Type
- Promotion Timeline
- SHAP Feature Importance

### Forecast Dashboard

- Actual vs Predicted Sales
- Prediction Error
- Forecast Trend
- Inventory Recommendation
- Forecast Accuracy

---

# Business Insights

- Promotional campaigns were associated with higher daily sales across most stores.
- Sales exhibited strong weekly and seasonal patterns.
- Historical sales (lag features) were the strongest predictors of future sales.
- Store type and assortment significantly influenced revenue.
- Competition distance showed comparatively lower impact on sales.
- Forecasting can support proactive inventory planning and workforce allocation.

---

# Business Recommendations

- Increase inventory before forecasted high-demand periods.
- Prioritize promotions for stores with historically strong promotional response.
- Optimize staffing using predicted sales trends.
- Monitor underperforming stores for operational improvements.
- Use forecasting to improve replenishment planning and reduce stockouts.

---

# Future Improvements

- Integrate weather and economic indicators
- Include local event and festival data
- Deploy the model using FastAPI
- Automate daily retraining
- Implement deep learning forecasting models (LSTM/Temporal Fusion Transformer)
- Build a real-time forecasting dashboard

---

# Dashboard Preview

![Dashboard](assets/dash1.png)
----
![Dashboard](assets/dash2.png)
----
![Dashboard](assets/dash3.png)
---
![Dashboard](assets/dash4.png)
---

# Repository

```
data/
dashboard/
images/
models/
notebooks/
reports/
README.md
requirements.txt
```

---

# Author

**P S**

Aspiring Data Scientist | Data Analyst

