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
   - DecisionTree
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
  
  ![image](https://github.com/user-attachments/assets/91422ae8-9e21-4ad8-831f-667b1e0ee3c7)

  - Bar plots (Delivery Times by Vehicle Type, Weather, Traffic, Area)
  
  ![image](https://github.com/user-attachments/assets/bc4a525e-6309-47b3-9c58-da108f23888e)

  ![image](https://github.com/user-attachments/assets/6ce8ecd0-3eaf-453b-be57-1d1818762538)

  ![image](https://github.com/user-attachments/assets/ca052822-44ad-4a7e-97b2-cf3ea42aca50)

  ![image](https://github.com/user-attachments/assets/90f4d29c-784a-4d28-9162-639285bf1f0e)

  - Heatmaps (correlations)
  
  ![image](https://github.com/user-attachments/assets/cafef2ff-65dc-4891-ab89-44f018725588)

## 🏆 Results
By the end of this project, achieve:
- A **cleaned and processed dataset** for modeling.
- Multiple **regression models** developed & tracked in MLflow(**http://127.0.0.1:5000/**).
  
  ![ml1](https://github.com/user-attachments/assets/d46902d6-760c-44b2-bcb4-862a693d156c)

  ![eva](https://github.com/user-attachments/assets/e4560ebd-acc5-4d54-947d-36e25fc56619)

  ![tuned](https://github.com/user-attachments/assets/be636e5d-e8a0-4de3-9ea4-72d287e9a490)


- A functional **Streamlit application** for delivery time prediction.

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
