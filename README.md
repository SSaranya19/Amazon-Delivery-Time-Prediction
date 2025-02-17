# Amazon-Delivery-Time-Prediction 🚚⏱️

## Problem Statement

This project aims to predict delivery times for e-commerce orders by leveraging a variety of factors like product size, distance, traffic conditions, and shipping methods. By analyzing the provided dataset, the goal is to build accurate regression models to estimate delivery times. The final product will feature a user-friendly interface, allowing users to input details and receive real-time delivery time predictions.

## Business Use Cases 📦

- **Enhanced Delivery Logistics:** 
  - Predict delivery times to improve customer satisfaction and optimize delivery schedules.
  
- **Dynamic Traffic and Weather Adjustments:**
  - Adjust delivery estimates based on current traffic and weather conditions.

- **Agent Performance Evaluation:**
  - Evaluate agent efficiency, identify areas for training or improvement.

- **Operational Efficiency:**
  - Optimize resource allocation by analyzing trends and performance metrics.

## Approach 🔍

1. **Data Preparation:**
   - Load and preprocess the dataset.
   - Handle missing or inconsistent data.
   - Perform feature engineering, such as calculating distances between store and drop locations.

2. **Data Cleaning:**
   - Remove duplicates and handle missing values.
   - Standardize categorical variables (e.g., weather, traffic conditions).

3. **Exploratory Data Analysis (EDA):**
   - Analyze trends in delivery times, agent performance, and external factors.
   - Visualize the impact of traffic, weather, and other variables on delivery times.

4. **Feature Engineering:**
   - Calculate geospatial distances using store and drop coordinates.
   - Extract time-based features like hour of the day and day of the week.

5. **Regression Model Development:**
   - Train multiple regression models:
     - Linear Regression
     - Random Forest Regressor
     - Gradient Boosting Regressor
   - Evaluate models using metrics like RMSE, MAE, and R-squared.
   - Compare models and track performance metrics using **MLflow**.

6. **Application Development:**
   - Build a user interface using **Streamlit** to:
     - Input order details (e.g., distance, traffic, weather).
     - Display predicted delivery times.

7. **Model Comparison and Tracking:**
   - Use **MLflow** to log, compare, and manage regression models.
   - Document hyperparameters, performance metrics, and model versions.

8. **Deployment:**
   - Deploy the application on **Streamlit** for accessibility and scalability.

## Dataset 📊

### `amazon_delivery.csv`

This dataset contains detailed information about orders, agents, and delivery conditions:

- **Order_ID**: Unique identifier for each order.
- **Agent_Age**: Age of the delivery agent.
- **Agent_Rating**: Rating of the delivery agent.
- **Store_Latitude/Longitude**: Geographic location of the store.
- **Drop_Latitude/Longitude**: Geographic location of the delivery address.
- **Order_Date/Order_Time**: Date and time when the order was placed.
- **Pickup_Time**: Time when the delivery agent picked up the order.
- **Weather**: Weather conditions during delivery.
- **Traffic**: Traffic conditions during delivery.
- **Vehicle**: Mode of transportation used for delivery.
- **Area**: Type of delivery area (Urban/Metropolitan).
- **Delivery_Time**: Target variable representing the actual time taken for delivery (in hours).
- **Category**: Category of the product being delivered.

## Data Flow and Architecture 🌐

1. **Data Preparation:**
   - Load and preprocess the dataset.
   - Store processed data locally for model development.

2. **Processing Pipeline:**
   - Perform feature engineering and data preprocessing.
   - Train and save regression models.

3. **Model Training:**
   - Utilize libraries like **scikit-learn** and **XGBoost** for model development.
   - Track model training and evaluation in **MLflow**.
   - Save trained models for deployment.

4. **Deployment:**
   - Use **Streamlit** to create a user-friendly front end for real-time delivery time prediction.

## Exploratory Data Analysis (EDA) 📈

Key insights and trends explored:

- Distribution of delivery times.
- Impact of weather and traffic on delivery times.
- Relationship between distance and delivery time.
- Agent performance across different conditions.

### Key Visualizations:
- **Bar charts**: Delivery times by product category.
- **Scatter plots**: Distance vs. delivery time.
- **Heatmaps**: Correlation between agent rating and delivery time.

## Results 🎯

By the end of this project, learners will achieve:

1. A cleaned and processed dataset ready for modeling.
2. Multiple regression models developed and tracked using **MLflow**.
3. Insights into the factors influencing delivery times.
4. A fully functional delivery time prediction system accessible via a **Streamlit** interface.

## Technical Tags 🧑‍💻

- Python
- Regression Modeling
- Data Cleaning
- Feature Engineering
- Streamlit
- MLflow

## Deliverables 📦

1. **Source Code:**
   - Python scripts for data preparation, EDA, feature engineering, and model development.

2. **Processed Data:**
   - Cleaned and prepared dataset for analysis.

3. **Regression Models:**
   - Trained and evaluated models for delivery time prediction.

4. **Application Code:**
   - Streamlit app code with prediction capabilities.

5. **Documentation:**
   - Detailed documentation explaining the implementation and results.

6. **Model Tracking:**
   - MLflow logs and comparisons of all regression models.

## Getting Started 🚀

To get started with this project:

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

Enjoy building and predicting! 😃

---

For more details or to contribute, feel free to open an issue or pull request! 🎉
