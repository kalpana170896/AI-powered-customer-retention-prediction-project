import pickle
import os
def save_model(model):

    with open("customer_churn_model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("Model Saved Successfully")

def save_scaler(scaler):
    with open("scaler.pkl", "wb") as file:
        pickle.dump(scaler, file)
        print("scaler saved successfully")

        print(os.path.exists("scaler.pkl"))