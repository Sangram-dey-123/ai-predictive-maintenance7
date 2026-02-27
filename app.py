import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Train model inside app (no pickle needed)
@st.cache_resource
def train_model():
    np.random.seed(42)

    data = pd.DataFrame({
        "Temperature": np.random.normal(75, 10, 1000),
        "Vibration": np.random.normal(50, 5, 1000),
        "Pressure": np.random.normal(30, 3, 1000),
        "Humidity": np.random.normal(40, 10, 1000)
    })

    data["Failure"] = (
        (data["Temperature"] > 85) |
        (data["Vibration"] > 60) |
        (data["Pressure"] > 35)
    ).astype(int)

    X = data.drop("Failure", axis=1)
    y = data["Failure"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model

model = train_model()

st.title("AI-Based Predictive Maintenance System")

temperature = st.slider("Temperature", 40, 120, 75)
vibration = st.slider("Vibration", 20, 100, 50)
pressure = st.slider("Pressure", 10, 60, 30)
humidity = st.slider("Humidity", 10, 100, 40)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Vibration": vibration,
        "Pressure": pressure,
        "Humidity": humidity
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Likely!")
    else:
        st.success("✅ Machine Operating Normally")
