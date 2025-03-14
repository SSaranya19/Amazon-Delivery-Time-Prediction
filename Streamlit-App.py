import streamlit as st 
import pandas as pd
import pickle

# Load the model
with open("Gradient Boosting.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Set page configuration
st.set_page_config(
    page_title="Amazon Delivery Time Predictor",
    page_icon="📦",
    layout="wide"
)

# Title of the app
st.title("📦 Amazon Delivery Time Prediction")

# Input fields for user data based on the available features
st.sidebar.header("📝 Input Order Details")

agent_age = st.sidebar.number_input("Agent Age 👤", min_value=18, max_value=100, value=30, step=1)
agent_rating = st.sidebar.number_input("Agent Rating ⭐", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
distance = st.sidebar.number_input("Distance (km) 📏", min_value=1.0, max_value=500.0, value=10.0, step=0.1)
weather = st.sidebar.selectbox("Weather 🌤️(0=Cloudy, 1=Fog, 2=Sandstorms, 3=Stormy, 4=Sunny, 5=Windy)", options=[0, 1, 2, 3, 4, 5])
traffic = st.sidebar.selectbox("Traffic Level 🚦(0=High, 1=Jam, 2=Low, 3=Medium)", options=[0, 1, 2, 3])
vehicle = st.sidebar.selectbox("Vehicle Type 🚗(0=bicycle, 1=motorcycle, 2=scooter, 3=van)", options=[0, 1, 2, 3])
area = st.sidebar.selectbox("Area Type 🏙️(0=Metropolitian, 1=Other, 2=Semi-Urban, 3=Urban)", options=[0, 1, 2, 3])
category = st.sidebar.selectbox("Category 📦(0=Apparel, 1=Books, 2=Clothing, 3=Cosmetics, 4=Electronics, 5=Grocery, 6=Home, 7=Jewelry, 8=Kitchen, 9=Outdoors, 10=Pet Supplie, 11=Shoes, 12=Skincare, 13=Snacks, 14=Sports, 15=Toys)", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
order_to_pickup_time = st.sidebar.number_input("Order To Pickup (minutes) ⏱️", min_value=0, max_value=1440, value=30, step=1)

# ✅ Manually define the correct feature order (matching training data)
feature_order = [
    'Agent_Age', 'Agent_Rating', 'Distance', 'Weather_Encoded', 'Traffic_Encoded', 'Vehicle_Encoded', 'Area_Encoded', 
    'Category_Encoded', 'Order_to_Pickup_Minutes'
]

# Prepare the input data as a DataFrame
input_data = pd.DataFrame([[agent_age, agent_rating, distance, weather, traffic,
                            vehicle, area, category, order_to_pickup_time]], 
                          columns=feature_order)

# ✅ Convert data types to match training data
input_data = input_data.astype(float)  

#📊 Show order summary
st.subheader("🔎 Order Summary")

order_summary_df = pd.DataFrame({
    "Field": ["Agent Age", "Agent Rating", "Distance (km)", "Weather", "Traffic Level", "Vehicle Type", "Area Type", "Category", "Order to Pickup (minutes)"],
    "Value": [
        agent_age,
        agent_rating,
        distance,
        ["Cloudy", "Fog", "Sandstorms", "Stormy", "Sunny", "Windy"][weather],
        ["High", "Jam", "Low", "Medium"][traffic],
        ["Bicycle", "Motorcycle", "Scooter", "Van"][vehicle],
        ["Metropolitan", "Other", "Semi-Urban", "Urban"][area],
        ["Apparel", "Books", "Clothing", "Cosmetics", "Electronics", "Grocery", "Home", "Jewelry", "Kitchen", "Outdoors", "Pet Supplies", "Shoes", "Skincare", "Snacks", "Sports", "Toys"][category],
        order_to_pickup_time
    ]
})

# Convert all values to strings to avoid Arrow errors
order_summary_df["Value"] = order_summary_df["Value"].astype(str)
st.dataframe(order_summary_df, use_container_width=True)

# 🚀 Make Prediction
if st.button("🚀 Predict Delivery Time"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🕒 Estimated Delivery Time: {prediction[0]:.2f} minutes")

        # Key Insights
        st.subheader("🔑 Key Insights")
        if distance > 100:
            st.write("📏 **Long Distance Alert:** The delivery distance is quite long, which may increase delivery time.")
        if traffic == 0 or traffic == 1:
            st.write("🚦 **High Traffic Alert:** Traffic conditions are likely to delay the delivery.")
        if weather == 2 or weather == 3:
            st.write("🌪️ **Bad Weather Alert:** Adverse weather conditions may slow down the delivery.")
        if vehicle == 0:
            st.write("🚴 **Vehicle Type Alert:** Using a bicycle for delivery may increase the delivery time.")

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")

# Reset button
if st.sidebar.button("🔄 Reset Predictions"):
    if 'predictions' in st.session_state:
        st.session_state.predictions = []
    st.success("Predictions have been reset!")