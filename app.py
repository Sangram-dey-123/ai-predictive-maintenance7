import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("AI-Based Predictive Maintenance System")

temperature = st.slider("Temperature", 40, 120, 75)
vibration = st.slider("Vibration", 20, 100, 50)
pressure = st.slider("Pressure", 10, 60, 30)
humidity = st.slider("Humidity", 10, 100, 40)

if st.button("Predict"):
    input_data = np.array([[temperature, vibration, pressure, humidity]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Likely!")
    else:
        st.success("✅ Machine Operating Normally")