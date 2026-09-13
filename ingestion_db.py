import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging configuration
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create SQLite database connection
engine = create_engine("sqlite:///inventory.db")

# Function to ingest a dataframe into the database
def ingest_db(df, table_name, engine):
    """This function will ingest the dataframe into a database table."""
    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

# Function to load all CSV files and ingest them into SQLite
def load_raw_data():
    """This function will load the CSV files as dataframes and ingest them into the database."""
    start = time.time()

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            file_path = os.path.join("data", file)
            df = pd.read_csv(file_path)

            logging.info(f"Ingesting {file} in db")

            table_name = file[:-4]
            ingest_db(df, table_name, engine)

    end = time.time()
    total_time = (end - start) / 60

    logging.info("---------------Ingestion Complete---------------")
    logging.info(f"Total Time Taken: {total_time} minutes")

if __name__ == "__main__":
    load_raw_data()