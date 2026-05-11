import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("models/fraud_detection_model.pkl")

st.title("Credit Card Fraud Detection App")

st.write("Enter transaction features below:")

features = []

for i in range(30):
    value = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(value)

if st.button("Predict"):

    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Normal Transaction")