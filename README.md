# Amazon-Delivery-Time-Prediction 🚚⏱️

## 📌 Project Overview
This project aims to predict delivery times for e-commerce orders based on factors such as product size, distance, traffic conditions, and shipping methods. By leveraging machine learning techniques, we develop regression models to estimate delivery times accurately. A user-friendly **Streamlit** application allows users to input order details and receive estimated delivery times.

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
6. Evaluation using RMSE, MAE, R²
7. Model tracking with MLflow
8. **Application Development:** Build a **Streamlit** UI for user inputs and predictions.
9. **Model Comparison & Tracking:** Log, compare, and manage different regression models with **MLflow**.
10. **Deployment:** Deploy the application using **Streamlit**.

## 📊 Dataset: `amazon_delivery.csv`
The dataset includes:
- **Order Details:** Order ID, date, time.
- **Agent Information:** Age, rating.
- **Location Data:** Store & drop coordinates.
- **Delivery Conditions:** Weather, traffic, vehicle type.
- **Target Variable:** Delivery time.

## 🔍 Exploratory Data Analysis (EDA)
- **Key Insights:**
  - Distribution of delivery times.
  - Impact of weather and traffic.
  - Correlations between numerical variables
- **Visualizations:**
  - Histplot charts (Distribution of Delivery Time)
  
  ![image](https://github.com/user-attachments/assets/eb303898-626a-49d6-b0e6-e85f29df43f8)
  - Box plots (Delivery Times by Vehicle Type, Weather, Traffic, Area)
  
  ![image](https://github.com/user-attachments/assets/260b2d3a-3797-42cf-9e0c-74d26863ca1e)

  ![image](https://github.com/user-attachments/assets/376fecbe-b645-438f-a1d8-39f21444a13c)

  ![image](https://github.com/user-attachments/assets/2da8455b-423f-44b8-af20-19ae1d6e42b5)

  ![image](https://github.com/user-attachments/assets/9292bf22-5401-4c4d-ac30-a5cb5736e577)
    
  - Heatmaps (correlations)
    
  ![image](https://github.com/user-attachments/assets/dd939e04-cf29-4a31-bc7f-74fb92a63498)



## 🏆 Results
By the end of this project, achieve:
- A **cleaned and processed dataset** for modeling.
- Multiple **regression models** developed & tracked in MLflow(**http://127.0.0.1:5000/**).
  
  ![image](https://github.com/user-attachments/assets/3f465333-e9e1-42c8-b5e2-67b7eb44baac)

  ![image](https://github.com/user-attachments/assets/252f08b8-6149-406f-b6fa-b11f4b628a0d)

- A functional **Streamlit application** for delivery time prediction.
- **Streamlit application** Link.
  
  https://amazondeliverytimeprediction.streamlit.app/

  ![stream](https://github.com/user-attachments/assets/fbe99815-3e5c-4378-95c0-df4768da670f)



## 🛠 Tech Stack
- **Programming:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
- **Model Tracking:** MLflow
- **Frontend:** Streamlit

## 🛠 Skills Learned
- Python scripting
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning (Regression Modeling)
- Model Tracking using MLflow
- Streamlit Application Development

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
   git clone https://github.com/SSaranya19/Amazon-Delivery-Time-Prediction.git
   cd Amazon-Delivery-Time-Prediction
