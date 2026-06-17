import logging
import sys

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    try:
        logger.info("Duplicate Value Handling Started")

        before_duplicates = df.duplicated().sum()

        logger.info(f"Duplicate Rows Before Removal : {before_duplicates}" )

        df = df.drop_duplicates()

        after_duplicates = df.duplicated().sum()

        logger.info(f"Duplicate Rows After Removal : {after_duplicates}" )

        logger.info( f"Dataset Shape After Removing Duplicates : {df.shape}")

        logger.info( "Duplicate Value Handling Successfully Completed" )

        return df

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()

        logger.warning(
            f"error in line no : {er_line.tb_lineno} : "
            f"due to : {er_type} and reason : {er_msg}"
        )



