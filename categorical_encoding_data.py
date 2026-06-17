import pandas as pd
import logging
import sys

logger = logging.getLogger(__name__)

def encoding(df):
    try:
        logger.info("Encoding Started")

        # Gender
        df["gender"] = df["gender"].map({ "Male": 1, "Female": 0 })

        # Yes / No columns
        yes_no_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
        for col in yes_no_cols:
            df[col] = df[col].map({"Yes": 1, "No": 0})  #dont apply mapping to all columns because they have interconnection one to one they from some times null values thats way we write this

        multi_cols = ['MultipleLines',      #remaining columns all we give another new variabel
                'InternetService',
                'OnlineSecurity',
                'OnlineBackup',
                'DeviceProtection',
                'TechSupport',
                'StreamingTV',
                'StreamingMovies',
                'Contract',
                'PaymentMethod',
                'SIM' ]

        df = pd.get_dummies( df, columns=multi_cols, drop_first=True ) #categorical columns convert to numerical columns thats way we use get_dummies

        logger.info("Encoding Completed Successfully")

        print(df.isnull().sum())

        return df

    except Exception as e:
     er_type, er_msg, er_line = sys.exc_info()

    logger.warning( f"error in line no : {er_line.tb_lineno} : " f"due to : {er_type} and reason : {er_msg}" )

    return df
