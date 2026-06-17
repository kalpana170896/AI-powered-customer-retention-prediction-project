from sklearn.model_selection import train_test_split
import logging
import sys

logger = logging.getLogger(__name__)

def split_data(df):
    try:
        logger.info("Train Test Split Started")

        X = df.drop("Churn", axis=1)
        y = df["Churn"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y )

        logger.info(f"X_train Shape : {X_train.shape}")
        logger.info(f"X_test Shape : {X_test.shape}")
        logger.info(f"y_train Shape : {y_train.shape}")
        logger.info(f"y_test Shape : {y_test.shape}")

        return X_train, X_test, y_train, y_test

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()

        logger.warning( f"error in line no : {er_line.tb_lineno} :"f"due to : {er_type} and reason : {er_msg}" )