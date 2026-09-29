import os
import pandas as pd
from sqlalchemy import create_engine
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")
url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
engine = create_engine(url)
with engine.connect() as conn:
    res = conn.execute(pd.io.sql.text("SHOW TABLES;")).fetchall()
    print(res)
