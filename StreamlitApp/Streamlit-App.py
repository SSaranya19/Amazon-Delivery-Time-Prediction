import streamlit as st 
import pandas as pd
import pickle

# Load the model
with open("Gradient Boosting.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Amazon Delivery Time Prediction")

# Input fields for user data based on the available features
st.header("Input Order Details")

agent_age = st.number_input("Agent Age", min_value=18, max_value=100, value=30, step=1)
agent_rating = st.number_input("Agent Rating", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
distance = st.number_input("Distance (km)", min_value=1.0, max_value=500.0, value=10.0, step=0.1)
weather = st.selectbox("Weather (0=Cloudy, 1=Fog, 2=Sandstorms, 3=Stormy, 4=Sunny, 5=Windy)", options=[0, 1, 2, 3, 4, 5])
traffic = st.selectbox("Traffic Level (0=High, 1=Jam, 2=Low, 3=Medium)", options=[0, 1, 2, 3])
vehicle = st.selectbox("Vehicle Type (0=bicycle, 1=motorcycle, 2=scooter, 3=van)", options=[0, 1, 2, 3])
area = st.selectbox("Area Type (0=Metropolitian, 1=Other, 2=Semi-Urban, 3=Urban)", options=[0, 1, 2, 3])
category = st.selectbox("Category Encoded (0=Apparel, 1=Books, 2=Clothing, 3=Cosmetics, 4=Electronics, 5=Grocery, 6=Home, 7=Jewelry, 8=Kitchen, 9=Outdoors, 10=Pet Supplie, 11=Shoes, 12=Skincare, 13=Snacks, 14=Sports, 15=Toys)", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
order_to_pickup_time = st.number_input("Order To Pickup (minutes)", min_value=0, max_value=1440, value=30, step=1)

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
st.write(input_data)

# 🚀 Make Prediction
if st.button("🚀 Predict Delivery Time"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🕒 Estimated Delivery Time: {prediction[0]:.2f} minutes")

        # Store predictions for min, max, avg calculations
        if 'predictions' not in st.session_state:
            st.session_state.predictions = []
        st.session_state.predictions.append(prediction[0])

        # Calculate min, max, avg
        min_time = min(st.session_state.predictions)
        max_time = max(st.session_state.predictions)
        avg_time = sum(st.session_state.predictions) / len(st.session_state.predictions)

        st.subheader("📊 Delivery Time Statistics")
        st.write(f"Minimum Predicted Delivery Time: {min_time:.2f} minutes")
        st.write(f"Maximum Predicted Delivery Time: {max_time:.2f} minutes")
        st.write(f"Average Predicted Delivery Time: {avg_time:.2f} minutes")

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
