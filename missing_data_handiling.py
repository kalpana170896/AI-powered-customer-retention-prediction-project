import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from log_code import setup_logging
logger = setup_logging("missing_data_handiling")

def missing(df):
    try:
        logger.info(f"no of null values : {(df.isnull().sum())}")
        logger.info(f"\n{df.isnull().sum()}")
        logger.info(f"no of blank values : {(df == ' ').sum()}")
        logger.info(f"\n{df == ''}")

        logger.info(f"==============before blank and null values==========")
        df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
        logger.info(f"=======after blank values convert to null values========")
        logger.info(f"no of null values : {(df.isnull().sum())}")
        logger.info(f"\n{df.isnull().sum()}")
        logger.info(f"no of blank values : {(df == ' ').sum()}")
        logger.info(f"\n{df == ''}")
        print(df.isnull().sum())

        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")  # total charges convert to numeric values
        median_value = df["TotalCharges"].median()  # median values calculation
        logger.info(f"median value = {median_value}")
        df["TotalCharges"] = df["TotalCharges"].fillna(median_value)  # null values replace the median values
        logger.info(f"Before Fill : {df['TotalCharges'].isnull().sum()}")
        df["TotalCharges"] = df["TotalCharges"].fillna(median_value)
        logger.info(f"After Fill : {df['TotalCharges'].isnull().sum()}")
        logger.info(f"\n{df.isnull().sum()}")
        return df
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.warning(f"error in line no : {er_line.tb_lineno} : due to : {er_type} and reason : {er_msg}")
