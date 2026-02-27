AI-Based Predictive Maintenance for Aerospace Launch Pad Systems

This project implements an AI-driven predictive maintenance framework for aerospace ground systems using Machine Learning and Deep Learning techniques.

It integrates **Isolation Forest** for anomaly detection and **LSTM (Long Short-Term Memory)** networks for Remaining Useful Life (RUL) prediction based on multi-sensor time-series data.


Problem Statement

Launch pad systems operate under extreme thermal, vibration, acoustic, and pressure conditions. Traditional maintenance strategies are either reactive (after failure) or preventive (fixed schedule-based), which do not capture real-time degradation patterns.

This project proposes an intelligent predictive maintenance solution to detect anomalies early and estimate Remaining Useful Life (RUL) accurately.


Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  
- TensorFlow / Keras  
- Streamlit  


AI/ML Models Used

Isolation Forest

- Used for anomaly detection  
- Identifies abnormal sensor behavior  
- Helps detect early system failures  

 LSTM Neural Network
 
- Used for time-series modeling  
- Predicts Remaining Useful Life (RUL)  
- Captures nonlinear temporal dependencies  

 System Architecture

Multi-Sensor Data  
↓  
Preprocessing & Normalization  
↓  
Isolation Forest (Anomaly Detection)  
↓  
LSTM Model (RUL Prediction)  
↓  
Streamlit Dashboard  


Live Deployment

Streamlit App Link:

 https://ai-predictive-maintenance7-plcblwz73keaodrabwglzw.streamlit.app/

---

 Project Structure

```
ai-predictive-maintenance7/
│
├── app.py
├── train_model.py
├── requirements.txt
├── lstm_rul_model.keras
└── README.md
```

---

 How to Run Locally

Step 1: Clone Repository

```
git clone https://github.com/Sangram-dey-123/ai-predictive-maintenance7.git
cd ai-predictive-maintenance7
```

Step 2: Install Dependencies

```
pip install -r requirements.txt
```

Step 3: Run Streamlit App

```
streamlit run app.py
```

Model Evaluation Metrics

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

 Key Features

- Multi-sensor time-series data simulation  
- Anomaly detection using Isolation Forest  
- Deep learning-based RUL prediction  
- Interactive Streamlit dashboard  
- Permanent cloud deployment  


Industry Relevance

- Aerospace ground system maintenance  
- Industry 4.0 predictive analytics  
- Intelligent infrastructure monitoring  


 Academic Details

Course: M.Tech – Term Paper I  
Domain: Artificial Intelligence / Aerospace Systems  
University: Alliance School of Advanced Computing  


 Author
 Sangram Dey 
 GitHub: https://github.com/Sangram-dey-123/ai-predictive-maintenance7  
