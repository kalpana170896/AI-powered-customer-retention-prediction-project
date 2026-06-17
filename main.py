import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings
warnings.filterwarnings("ignore")
import logging as log
import sys
from log_code import setup_logging
logger = setup_logging("main")
from sklearn.model_selection import train_test_split
from missing_data_handiling import missing
from duplicates_data_handiling import remove_duplicates
from categorical_encoding_data import encoding
from feature_scaling_data import scaling
from train_test_split_data import split_data
from model_training_data import train_model
from model_training_data import train_model
from model_saving_data import save_model,save_scaler
import os
class TELCO_CUSTOMER:
    def __init__(self,path):
        try:
           self.path = path
           self.df = pd.read_csv(self.path) #reading the dataset
           logger.info(f"the shape of the data was : {self.df.shape}")

           self.df["SIM"] = np.random.choice(
               ["Jio", "Airtel", "Vodafone", "BSNL"],
               size=len(self.df))
           self.df.to_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv", index=False)
           print("SIM column added successfully")
           print(self.df)
        except Exception as e:
            er_type , er_msg , er_line = sys.exc_info()
            logger.warning(f"error in line no : {er_line.tb_lineno} : due to : {er_type} and reason : {er_msg}")

    def handiling_missing_values(missing):
           #'we are go to use techniques in median techniqu for handiling missing values
        try:
            pass
        except Exception as e:
            er_type , er_msg , er_line = sys.exc_info()
            logger.warning(f"error in line no : {er_line.tb_lineno} : due to : {er_type} and reason : {er_msg}")




if __name__ == "__main__":
        try:
          obj = TELCO_CUSTOMER("WA_Fn-UseC_-Telco-Customer-Churn.csv")
          obj.handiling_missing_values()
          obj.df =  missing(obj.df)
          obj.df = remove_duplicates(obj.df)
          print("Final Shape :", obj.df.shape)
          print("Duplicate Count :", obj.df.duplicated().sum())
          print(obj.df.shape)
          obj.df = encoding(obj.df)
          obj.df,scaler = scaling(obj.df)
          print(obj.df.head())
          print(obj.df[["tenure","MonthlyCharges","TotalCharges"]].head())

          print("Before Drop:", obj.df.shape)

          obj.df = obj.df.drop("customerID", axis=1) #customer id not use for prediction that's way delete that column

          print("After Drop:", obj.df.shape)

          print(obj.df.head())

          X_train, X_test, y_train, y_test = split_data(obj.df)
          print(X_train.shape)
          print(X_test.shape)
          print(y_train.shape)
          print(y_test.shape)
          print(X_train.head())
          print(y_train.head())

          model = train_model(
            X_train,
            X_test,
            y_train,
            y_test )

          print("Train Accuracy :", model.score(X_train, y_train))
          print("Test Accuracy :", model.score(X_test, y_test))


          model = train_model(X_train, X_test, y_train, y_test)
          X_train.columns.tolist()


          print(X_train.columns)

          obj.df, scaler = scaling(obj.df)
          save_model(model)
          save_scaler(scaler)

          print(type(model))
          print(type(scaler))
          print(os.path.exists("scaler.pkl"))



          print(os.path.exists("customer_churn_model.pkl"))
          print(os.path.exists("scaler.pkl"))



          print("Model File :", os.path.exists("customer_churn_model.pkl"))
          print("Scaler File :", os.path.exists("scaler.pkl"))

        except Exception as e:
           er_type, er_msg, er_line = sys.exc_info()
           logger.warning(f"error in line no : {er_line.tb_lineno} : due to : {er_type} and reason : {er_msg}")
