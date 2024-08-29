""" Script for tranferring .csv file data to MySQL table """

import os
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

db_user: str = os.environ.get('USER') or ""
db_password: str = os.environ.get('PWD') or ""
db_host = os.environ.get('HOST') or ""
db_port = os.environ.get('PORT') or ""
db_name = os.environ.get('DB') or ""
csv_file_path = os.environ.get('SRC') or ""
table_name = os.environ.get('DEST') or ""

engine: sqlalchemy.engine.base.Engine = create_engine(
    f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')


def main() -> None:
    try:
        df: pd.DataFrame = pd.read_csv(csv_file_path)
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print("Data imported successfully!")
    except Exception as e:
        print({"error": str(e)})


if __name__ == "__main__":
    main()
