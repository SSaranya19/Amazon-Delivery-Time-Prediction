# Amazon-Delivery-Time-Prediction 🚚⏱️

## 📌 Project Overview
This project aims to predict delivery times for e-commerce orders based on factors such as product size, distance, traffic conditions, and shipping methods. By leveraging machine learning techniques, we develop regression models to estimate delivery times accurately. A user-friendly **Streamlit** application allows users to input order details and receive estimated delivery times.

## 🛠 Skills Learned
- Python scripting
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning (Regression Modeling)
- Model Tracking using MLflow
- Streamlit Application Development

## 📦 Business Use Cases
- **Enhanced Delivery Logistics:** Predict delivery times to optimize schedules and improve customer satisfaction.
- **Dynamic Adjustments:** Adjust delivery estimates based on real-time traffic and weather conditions.
- **Agent Performance Evaluation:** Assess delivery agent efficiency.
- **Operational Efficiency:** Optimize resource allocation for deliveries.

## 🏗 Approach
1. **Data Preparation:** Load and preprocess the dataset, handle missing values, and perform feature engineering.
2. **Data Cleaning:** Remove duplicates, standardize categorical variables.
3. **EDA:** Analyze trends, visualize factors impacting delivery times.
4. **Feature Engineering:** Compute distances, extract time-based features.
5. **Regression Model Development:**
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
   - XGBRegressor
   - SVR
   - Evaluation using RMSE, MAE, R²
   - Model tracking with MLflow
6. **Application Development:** Build a **Streamlit** UI for user inputs and predictions.
7. **Model Comparison & Tracking:** Log, compare, and manage different regression models with **MLflow**.
8. **Deployment:** Deploy the application using **Streamlit**.

## 📊 Dataset: `amazon_delivery.csv`
The dataset includes:
- **Order Details:** Order ID, date, time.
- **Agent Information:** Age, rating.
- **Location Data:** Store & drop coordinates.
- **Delivery Conditions:** Weather, traffic, vehicle type.
- **Target Variable:** Delivery time in hours.

## 🔍 Exploratory Data Analysis (EDA)
- **Key Insights:**
  - Distribution of delivery times.
  - Impact of weather and traffic.
  - Distance vs. delivery time correlation.
  - Agent performance across conditions.
- **Visualizations:**
  - Bar charts (delivery times by product category)
  - Scatter plots (distance vs. delivery time)
  - Heatmaps (correlations)

## 🏆 Results
By the end of this project, we achieve:
- A **cleaned and processed dataset** for modeling.
- Multiple **regression models** developed & tracked in MLflow.
- Insights into factors influencing delivery times.
- A functional **Streamlit application** for delivery time prediction.

## 🛠 Tech Stack
- **Programming:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
- **Model Tracking:** MLflow
- **Frontend:** Streamlit

## 📁 Deliverables
1. **Source Code:** Python scripts for data processing, modeling.
2. **Processed Data:** Cleaned dataset for analysis.
3. **Regression Models:** Trained models for delivery time prediction.
4. **Application Code:** Streamlit-based UI.
5. **Documentation:** Implementation details & results.
6. **Model Tracking:** MLflow logs and model comparisons.

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
