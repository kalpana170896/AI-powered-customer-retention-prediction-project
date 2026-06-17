from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load Model
with open("customer_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        gender = 1 if request.form["gender"] == "Male" else 0

        SeniorCitizen = int(request.form["SeniorCitizen"])

        Partner = 1 if request.form["Partner"] == "Yes" else 0

        Dependents = 1 if request.form["Dependents"] == "Yes" else 0

        tenure = float(request.form["tenure"])

        PhoneService = 1 if request.form["PhoneService"] == "Yes" else 0

        PaperlessBilling = 1 if request.form["PaperlessBilling"] == "Yes" else 0

        MonthlyCharges = float(request.form["MonthlyCharges"])

        TotalCharges = float(request.form["TotalCharges"])


        data = {
            "gender":[gender],
            "SeniorCitizen":[SeniorCitizen],
            "Partner":[Partner],
            "Dependents":[Dependents],
            "tenure":[tenure],
            "PhoneService":[PhoneService],
            "PaperlessBilling":[PaperlessBilling],
            "MonthlyCharges":[MonthlyCharges],
            "TotalCharges":[TotalCharges],

            "MultipleLines_No phone service":[0],
            "MultipleLines_Yes":[0],

            "InternetService_Fiber optic":[0],
            "InternetService_No":[0],

            "OnlineSecurity_No internet service":[0],
            "OnlineSecurity_Yes":[0],

            "OnlineBackup_No internet service":[0],
            "OnlineBackup_Yes":[0],

            "DeviceProtection_No internet service":[0],
            "DeviceProtection_Yes":[0],

            "TechSupport_No internet service":[0],
            "TechSupport_Yes":[0],

            "StreamingTV_No internet service":[0],
            "StreamingTV_Yes":[0],

            "StreamingMovies_No internet service":[0],
            "StreamingMovies_Yes":[0],

            "Contract_One year":[0],
            "Contract_Two year":[0],

            "PaymentMethod_Credit card (automatic)":[0],
            "PaymentMethod_Electronic check":[0],
            "PaymentMethod_Mailed check":[0],

            "SIM_BSNL":[0],
            "SIM_Jio":[0],
            "SIM_Vodafone":[0]
        }

        df = pd.DataFrame(data)

        # Scaling
        df[["tenure","MonthlyCharges","TotalCharges"]] = scaler.transform(
            df[["tenure","MonthlyCharges","TotalCharges"]]
        )

        prediction = model.predict(df)[0]

        if prediction == 1:
            result = "Customer Will Churn"
        else:
            result = "Customer Will Not Churn"

        return render_template(
            "index.html",
            prediction=result)


    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
