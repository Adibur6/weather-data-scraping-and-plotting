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

    def save_data(self, data_dict):
        # Iterate through the dictionary items
        original=True and len(data_dict)>0
        try:
            with DBCM() as cursor:
                for sample_date, temp_data in data_dict.items():
                    if not self.is_valid_date(sample_date):
                        print(f"Invalid date format for {sample_date}. Data not saved.")
                        continue

                    # Check if the sample_date already exists in the database
                    cursor.execute('SELECT * FROM temperature WHERE sample_date = ?', (sample_date,))
                    existing_data = cursor.fetchone()

                    if existing_data:
                        print(f"Data for {sample_date} already exists. Not saving duplicate entry.")
                        original=False
                    else:
                        # Extract temperature data from the dictionary
                        min_temp = temp_data.get('Min', 0.0)
                        max_temp = temp_data.get('Max', 0.0)
                        avg_temp = temp_data.get('Mean', 0.0)

                        # Insert data into the 'temperature' table
                        cursor.execute('INSERT INTO temperature VALUES(NULL,?,?,?,?)', (sample_date, min_temp, max_temp, avg_temp))
                       
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        return original

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
