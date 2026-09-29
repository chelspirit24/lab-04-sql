#!/usr/bin/env python3
import os 
import logging
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

def get_data_by_group(value):
    """Retrieve all rows from the mock table where the `group` column equals the given value"""
    logging.info(f"Retrieving data for group: {value}")
    url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
    engine = create_engine(url)
    
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM mock WHERE `group` = %s"
    
    try:
        # pd.read_sql accepts the %s parameter format when passing params
        df = pd.read_sql(query, con=engine, params=(value,))
        logging.info(f"Successfully retrieved {len(df)} rows for group '{value}'")
        return df
    except Exception as e:
        logging.error(f"Error retrieving data by group: {e}")
        raise
    finally:
        engine.dispose()

def plot_counts(groupby): 
    """Count rows per distinct value of a given column and plot a bar chart"""
    logging.info(f"Plotting counts for column: {groupby}")
    url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
    engine = create_engine(url)
    
    # Constructing the GROUP BY query
    query = f"SELECT `{groupby}`, COUNT(*) as count FROM mock GROUP BY `{groupby}`;"
    
    try:
        df = pd.read_sql(query, con=engine)
        logging.info(f"Successfully retrieved counts for column '{groupby}'")
        
        # Plotting the results
        ax = df.plot.bar(x=groupby, y='count', title=f'Counts grouped by {groupby}')
        plt.xlabel(groupby)
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.error(f"Error plotting counts: {e}")
        raise
    finally:
        engine.dispose()

def main():
    """Main function to demonstrate querying and plotting."""
    print(f"--- Fetching data for group '2022-23' ---")
    data_df = get_data_by_group('2022-23')
    print(f"Returned {len(data_df)} rows.")
    if not data_df.empty:
        print("First few rows:")
        print(data_df.head())
        
    print("\n--- Plotting counts by group ---")
    plot_counts('group')

if __name__ == "__main__":
    main()