#!/usr/bin/env python3
import os 
import logging
from sqlalchemy import create_engine, text
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")
filename = "MOCK_DATA.csv"
table = "mock"

def read_data(filename):
    """Read data from a CSV file into a pandas DataFrame"""
    logging.info(f"Reading data from {filename}")
    # Load the CSV file using pandas
    return pd.read_csv(filename)

def clean_data(data):
    """Clean the data by removing missing values and enforcing correct data types"""
    logging.info("Cleaning data")
    # Drop rows with missing values
    cleaned_data = data.dropna().copy()
    
    # Convert goals columns to integers
    cleaned_data['home_goals'] = cleaned_data['home_goals'].astype(int)
    cleaned_data['away_goals'] = cleaned_data['away_goals'].astype(int)
    
    # Sort the data by the 'group' column
    cleaned_data = cleaned_data.sort_values(by='group', ascending=True)
    
    logging.info("Data cleaning completed successfully")
    return cleaned_data

def load_data(data, table):
    """Upload the cleaned data to a MySQL database"""
    logging.info(f"Uploading data to table: {table}")
    # Construct the database connection URL
    url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
    engine = create_engine(url)

    try: 
        # Upload data to the database, replacing the table if it already exists
        data.to_sql(table, con=engine, if_exists="replace", index=False)
        with engine.connect() as conn:
            # Verify the number of uploaded rows
            count = conn.execute(text(f"SELECT COUNT(*) FROM `{table}`")).scalar()
        logging.info(f"Uploaded {count} rows to {DBNAME}.{table}")
    except Exception as e:
        logging.error(f"Upload failed: {e}")
        raise
    finally:
        # Dispose of the engine to release resources
        engine.dispose()

def main(): 
    """Main function to execute the data processing pipeline"""
    logging.info("Starting data processing pipeline")
    # Step 1: Read the data
    data = read_data(filename)
    # Step 2: Clean the data
    cleaned_data = clean_data(data)
    # Step 3: Load the data into the database
    load_data(cleaned_data, table)
    
    logging.info("Pipeline executed successfully")

if __name__ == "__main__":
    main()