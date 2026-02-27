import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")