from dbcm import DBCM
import pandas as pd
from datetime import datetime
import sqlite3

class DBOperations:
    def fetch_data(self):
        try:
            with DBCM() as cursor:
                cursor.execute('SELECT * FROM temperature')
                all_data = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return pd.DataFrame()

        column_names = ['id', 'sample_date', 'min_temp', 'max_temp', 'avg_temp']
        df = pd.DataFrame(all_data, columns=column_names)
        return df

    def is_valid_date(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def save_data(self, sample_date, min_temp, max_temp, avg_temp):
        if not self.is_valid_date(sample_date):
            # print(f"Invalid date format for {sample_date}. Data not saved.")
            return False

        try:
            with DBCM() as cursor:
                # Check if the sample_date already exists in the database
                cursor.execute('SELECT * FROM temperature WHERE sample_date = ?', (sample_date,))
                existing_data = cursor.fetchone()

                if existing_data:
                    # print(f"Data for {sample_date} already exists. Not saving duplicate entry.")
                    return False
                else:
                    cursor.execute('INSERT INTO temperature VALUES(NULL,?,?,?,?)', (sample_date, min_temp, max_temp, avg_temp))
                    # print(f"Data for {sample_date} saved successfully.")
                    return True
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def initialize_db(self):
        try:
            with DBCM() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY, sample_date TEXT UNIQUE, min_temp REAL, max_temp REAL, avg_temp REAL)")
                print("Database created successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def purge_data(self):
        try:
            with DBCM() as cursor:
                cursor.execute('DELETE FROM temperature')
                print("Data purged successfully.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

