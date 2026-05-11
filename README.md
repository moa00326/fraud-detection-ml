# Credit Card Fraud Detection Using Machine Learning

This project detects fraudulent credit card transactions using machine learning techniques and a Streamlit web application for real-time prediction.

---

## Project Overview

The goal of this project is to identify fraudulent transactions from highly imbalanced financial transaction data.

The project includes:
- Data analysis
- Data visualization
- SMOTE oversampling
- Machine learning classification
- Model evaluation
- Streamlit deployment

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Streamlit
- Joblib

---

## Models Used

### Logistic Regression
Baseline model for fraud classification.

### Logistic Regression + SMOTE
Used to improve fraud recall on imbalanced data.

### Random Forest + SMOTE
Final production model with improved fraud detection performance.

---

## Final Model Performance

| Metric | Score |
|---|---|
| Precision | 0.87 |
| Recall | 0.85 |


::contentReference[oaicite:0]{index=0}


---

## Streamlit Web Application

The project includes a Streamlit app for real-time fraud prediction.

Features:
- User transaction inputs
- Real-time fraud prediction
- Interactive web interface
- Machine learning deployment

---

## Screenshots
## Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

## Streamlit App

![Streamlit App](images/streamlit_app.png)

Future Improvements
XGBoost integration
ROC curve optimization
Feature importance analysis
Cloud deployment
Real-time API integration
Author

Built by Tshego as a machine learning portfolio project focused on fraud analytics and real-time prediction systems.

## Project Structure

```text
fraud-detection-ml/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
├── images/
├── models/
│   └── fraud_detection_model.pkl
│
├── notebooks/
│   └── fraud_detection_model.ipynb

---






