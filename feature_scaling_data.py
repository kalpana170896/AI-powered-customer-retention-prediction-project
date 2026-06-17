from sklearn.preprocessing import StandardScaler
import logging
import sys

logger = logging.getLogger(__name__)

def scaling(df):
    try:
        logger.info("Feature Scaling Started")

        scaler = StandardScaler()

        num_cols = [
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
        ]

        df[num_cols] = scaler.fit_transform(df[num_cols])

        logger.info("Feature Scaling Completed")

        return df,scaler

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()

        logger.warning(
            f"error in line no : {er_line.tb_lineno} : "
            f"due to : {er_type} and reason : {er_msg}"
        )

        return df,None