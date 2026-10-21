import streamlit as st
import pandas as pd
import joblib

# Load the trained Decision Tree model
model = joblib.load("dt.sav")

# Application Title
st.title("🚚 Delivery Delay Prediction App")
st.write("Enter the delivery details below to predict if there will be a delivery delay.")

# Input fields matching the dataset features
st.header("Features Input")

delivery_distance = st.number_input("Delivery Distance (miles)", min_value=0.0, value=25.0)
traffic_congestion = st.slider("Traffic Congestion Level (1-5)", min_value=1, max_value=5, value=3)
weather_condition = st.slider("Weather Condition Score (1-5)", min_value=1, max_value=5, value=3)
delivery_slot = st.selectbox("Delivery Slot", options=[1, 2, 3], format_func=lambda x: f"Slot {x}")
driver_experience = st.number_input("Driver Experience (Years)", min_value=0, max_value=50, value=10)
num_stops = st.number_input("Number of Stops", min_value=0, max_value=20, value=4)
vehicle_age = st.number_input("Vehicle Age (Years)", min_value=0, max_value=30, value=5)
road_condition_score = st.slider("Road Condition Score (1-5)", min_value=1, max_value=5, value=3)
package_weight = st.number_input("Package Weight (lbs)", min_value=0.0, value=15.0)
fuel_efficiency = st.number_input("Fuel Efficiency (mpg)", min_value=0.0, value=12.0)
warehouse_processing_time = st.number_input("Warehouse Processing Time (minutes)", min_value=0, value=45)

# Predict button
if st.button("Predict Delay"):
    # Create feature dataframe
    input_data = pd.DataFrame([{
        'Delivery_Distance': delivery_distance,
        'Traffic_Congestion': traffic_congestion,
        'Weather_Condition': weather_condition,
        'Delivery_Slot': delivery_slot,
        'Driver_Experience': driver_experience,
        'Num_Stops': num_stops,
        'Vehicle_Age': vehicle_age,
        'Road_Condition_Score': road_condition_score,
        'Package_Weight': package_weight,
        'Fuel_Efficiency': fuel_efficiency,
        'Warehouse_Processing_Time': warehouse_processing_time
    }])

    # Predict
    prediction = model.predict(input_data)[0]
    
    # Output result
    if prediction == 1:
        st.error("⚠️ Prediction: The delivery is highly likely to be DELAYED.")
    else:
        st.success("✅ Prediction: The delivery will likely arrive ON TIME.")
