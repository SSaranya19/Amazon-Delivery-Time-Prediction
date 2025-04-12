import streamlit as st
import pandas as pd
import joblib
import datetime

# Load model
model = joblib.load("XGBoost_model.pkl")

# Page layout
st.set_page_config(page_title="Amazon Delivery Time Prediction", page_icon="📦", layout="wide")
st.title("🚚 Amazon Delivery Time Predictor")

# Input fields for user data based on the available features
st.sidebar.header("📝 Input Order Details")

agent_age = st.sidebar.number_input("Agent Age 👤", min_value=18, max_value=100, value=30)
agent_rating = st.sidebar.number_input("Agent Rating ⭐", min_value=0.0, max_value=5.0, value=4.5, step=0.1)
distance = st.sidebar.number_input("Distance (in km) 📏", min_value=0.1, max_value=500.0, value=15.0)
order_to_pickup_time = st.sidebar.number_input("Order to Pickup (minutes) ⏱️", min_value=0, max_value=1440, value=30)

# Date input for Order Day
order_date = st.sidebar.date_input("Order Date 📅", value=datetime.date.today())
order_day = order_date.day
order_dayname = order_date.strftime("%A")
order_month = order_date.month

# Dropdowns
weather_options = ["Fog", "Sandstorms", "Stormy", "Sunny", "Windy"]
vehicle_options = ["Motorcycle", "Scooter", "Van"]
area_options = ["Other", "Semi-Urban", "Urban"]
category_options = ["Books", "Clothing", "Cosmetics", "Electronics", "Grocery", "Home", "Jewelry", "Kitchen",
                    "Outdoors", "Pet Supplies", "Shoes", "Skincare", "Snacks", "Sports", "Toys"]
traffic_levels = ["Low", "Medium", "High", "Jam"]

# User Selections
weather = st.sidebar.selectbox("Weather 🌤️", weather_options)
vehicle = st.sidebar.selectbox("Vehicle Type 🚗", vehicle_options)
area = st.sidebar.selectbox("Area Type 🏙️", area_options)
category = st.sidebar.selectbox("Category 📦", category_options)
traffic = st.sidebar.selectbox("Traffic Level 🚦", traffic_levels)

# Ordinal Encoding
traffic_map = {"Low": 0, "Medium": 1, "High": 2, "Jam": 3}
dayname_map = {name: i for i, name in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
traffic_encoded = traffic_map[traffic]
order_dayname_encoded = dayname_map[order_dayname]

# Base numerical input
input_data = {
    "Agent_Age": agent_age,
    "Agent_Rating": agent_rating,
    "Traffic": traffic_encoded,
    "Distance_km": distance,
    "Order_to_Pickup_Minutes": order_to_pickup_time,
    "Order_Day": order_day,
    "Order_DayName": order_dayname_encoded,
    "Order_Month": order_month,
}

# Nominal One-hot Encoding
one_hot_columns = [
    "Weather_Fog", "Weather_Sandstorms", "Weather_Stormy", "Weather_Sunny", "Weather_Windy",
    "Vehicle_motorcycle ", "Vehicle_scooter ", "Vehicle_van",
    "Area_Other", "Area_Semi-Urban ", "Area_Urban ",
    "Category_Books", "Category_Clothing", "Category_Cosmetics", "Category_Electronics", "Category_Grocery",
    "Category_Home", "Category_Jewelry", "Category_Kitchen", "Category_Outdoors", "Category_Pet Supplies",
    "Category_Shoes", "Category_Skincare", "Category_Snacks", "Category_Sports", "Category_Toys"
]

# Initialize all one-hot columns to 0
for col in one_hot_columns:
    input_data[col] = 0

# Set selected one-hot values to 1
if f"Weather_{weather}" in one_hot_columns:
    input_data[f"Weather_{weather}"] = 1

vehicle_col_map = {
    "Motorcycle": "Vehicle_motorcycle ",
    "Scooter": "Vehicle_scooter ",
    "Van": "Vehicle_van"
}
input_data[vehicle_col_map[vehicle]] = 1

area_col_map = {
    "Other": "Area_Other",
    "Semi-Urban": "Area_Semi-Urban ",
    "Urban": "Area_Urban "
}
input_data[area_col_map[area]] = 1

category_col = f"Category_{category}"
if category_col in one_hot_columns:
    input_data[category_col] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# 🔍 Function to generate insights
def generate_insights(prediction, inputs):
    insights = []

    # Distance Insight
    if inputs["Distance_km"] > 30:
        insights.append("🛣️ The delivery distance is quite long, which increases delivery time.")
    elif inputs["Distance_km"] < 5:
        insights.append("📍 The delivery distance is short, likely reducing delivery time.")

    # Traffic Insight
    if inputs["Traffic"] == 3:
        insights.append("🚦 Heavy traffic (Jam) is expected to delay the delivery.")
    elif inputs["Traffic"] == 0:
        insights.append("✅ Low traffic allows faster delivery.")

    # Weather Insight
    if inputs.get("Weather_Stormy", 0) == 1 or inputs.get("Weather_Fog", 0) == 1:
        insights.append("🌧️ Bad weather conditions may slow down the delivery.")
    elif inputs.get("Weather_Sunny", 0) == 1:
        insights.append("☀️ Good weather helps ensure timely delivery.")

    # Agent Rating and Age
    if inputs["Agent_Rating"] >= 4.5:
        insights.append("🌟 The delivery agent has a high rating, indicating reliable service.")
    if inputs["Agent_Age"] < 25:
        insights.append("🧑‍💼 A younger agent may indicate faster but less experienced delivery.")
    elif inputs["Agent_Age"] > 50:
        insights.append("👨‍🦳 Experienced agent may ensure careful delivery.")

    # Order Day
    if inputs["Order_DayName"] in [5, 6]:  # Saturday/Sunday
        insights.append("📅 Weekend orders might face delays due to higher demand or fewer agents.")

    return insights


# Predict
if st.button("Predict Delivery Time 🕒"):
    # Display Order Summary
    st.subheader("📝 Order Summary")
    summary_data = {
        "Agent Age": agent_age,
        "Agent Rating": agent_rating,
        "Distance (km)": distance,
        "Order to Pickup Time (min)": order_to_pickup_time,
        "Order Date": order_date.strftime("%Y-%m-%d"),
        "Traffic": traffic,
        "Weather": weather,
        "Vehicle": vehicle,
        "Area": area,
        "Category": category
    }

    summary_df = pd.DataFrame({
        "Feature": list(summary_data.keys()),
        "Value": [str(v) for v in summary_data.values()]
    })
    st.table(summary_df)

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Delivery Time: **{round(prediction, 2)} minutes**")

    # 🧠 Show Key Insights
    st.subheader("🔍 Key Insights Based on Your Order")
    insights = generate_insights(prediction, input_data)
    for i, insight in enumerate(insights, 1):
        st.markdown(f"{i}. {insight}")
