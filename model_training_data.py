from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report)
import logging
import sys

def train_model(X_train, X_test, y_train, y_test):
    try:
                logger = logging.getLogger(__name__)
               # Train Model
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train, y_train)

                # Prediction
                y_pred = model.predict(X_test)

                # Test Accuracy
                test_accuracy = accuracy_score(y_test, y_pred)
                print("Test Accuracy :", test_accuracy)

                # Train Accuracy
                y_train_pred = model.predict(X_train)
                train_accuracy = accuracy_score(y_train, y_train_pred)
                print("Train Accuracy :", train_accuracy)

                # Metrics
                precision = precision_score(y_test, y_pred)
                recall = recall_score(y_test, y_pred)
                f1 = f1_score(y_test, y_pred)

                print("Precision :", precision)
                print("Recall :", recall)
                print("F1 Score :", f1)

                print("\nConfusion Matrix")
                print(confusion_matrix(y_test, y_pred))

                print("\nClassification Report")
                print(classification_report(y_test, y_pred))

                logger.info("Model Training Completed Successfully")

                return model

    except Exception as e:
                er_type, er_msg, er_line = sys.exc_info()

                logger.warning(
                    f"error in line no : {er_line.tb_lineno} : "
                    f"due to : {er_type} and reason : {er_msg}"
                )



