# AI-powered-customer-retention-prediction-project
# 🚀 AI Powered Customer Retention Prediction System

## 📌 Project Overview

The AI Powered Customer Retention Prediction System is a Machine Learning web application that predicts whether a telecom customer is likely to churn or stay with the company.

This project helps businesses identify customers who are at risk of leaving, allowing them to take proactive retention measures and improve customer satisfaction.

---

## 🎯 Project Objectives

* Predict customer churn using Machine Learning.
* Analyze customer behavior and service usage patterns.
* Build an end-to-end ML pipeline.
* Deploy the model using Flask.
* Provide real-time churn predictions through a user-friendly web interface.

---

## 📊 Dataset Information

Dataset: Telco Customer Churn Dataset

Features include:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Paperless Billing
* Monthly Charges
* Total Charges
* Internet Services
* Online Security
* Tech Support
* Contract Type
* Payment Method
* SIM Provider
* Churn Status

---

## ⚙️ Machine Learning Pipeline

### 1. Data Collection

* Loaded telecom customer churn dataset.

### 2. Data Preprocessing

* Missing Value Handling
* Duplicate Removal
* Categorical Encoding
* Feature Scaling

### 3. Feature Engineering

* Added SIM Provider feature.
* Converted categorical variables into numerical format.

### 4. Data Splitting

* Train-Test Split (80:20)

### 5. Model Training

* Logistic Regression Algorithm

### 6. Model Evaluation

Metrics Used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

---

## 📈 Model Performance

| Metric            | Score  |
| ----------------- | ------ |
| Training Accuracy | ~80.6% |
| Testing Accuracy  | ~80.7% |
| Precision         | ~65.8% |
| Recall            | ~56.6% |
| F1 Score          | ~60.9% |

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Pickle

### Web Framework

* Flask

### Deployment

* Render

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AI-Powered-Customer-Retention-Prediction/
│
├── app.py
├── main.py
├── Procfile
├── requirements.txt
├── README.md
│
├── customer_churn_model.pkl
├── scaler.pkl
│
├── templates/
│   └── index.html
│
├── logs/
│
├── missing_data_handiling.py
├── duplicates_data_handiling.py
├── categorical_encoding_data.py
├── feature_scaling_data.py
├── train_test_split_data.py
├── model_training_data.py
├── model_saving_data.py
│
└── WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

## 🌐 Web Application Features

✅ Customer Churn Prediction

✅ Beautiful User Interface

✅ Real-Time Prediction

✅ Machine Learning Integration

✅ Model & Scaler Serialization

✅ Flask Deployment Ready

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Customer-Retention-Prediction.git
```

### Move to Project Directory

```bash
cd AI-Powered-Customer-Retention-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```


## 🔮 Future Improvements

* Random Forest Model
* XGBoost Model
* Hyperparameter Tuning
* Feature Importance Analysis
* Customer Retention Recommendations
* Cloud Deployment Enhancements

---

## 👩‍💻 Author

Kalpana

Machine Learning & Data analyst

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub and support the project.
