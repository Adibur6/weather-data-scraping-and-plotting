import sqlite3
import pandas as pd

class DBOperations:
    def fetch_data(self):
        connection = sqlite3.connect('Temperature.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM temperature')
        all_data = cursor.fetchall()
        connection.close()
        
        # Convert the fetched data to a DataFrame with column names
        column_names = ['id', 'sample_date', 'min_temp', 'max_temp', 'avg_temp']
        df = pd.DataFrame(all_data, columns=column_names)
        return df
        
    def save_data(self, sample_date, min_temp, max_temp, avg_temp):
        connection = sqlite3.connect('Temperature.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO temperature VALUES(NULL,?,?,?,?)', (sample_date, min_temp, max_temp, avg_temp))
        connection.commit()
        connection.close()
        
    def initialize_db(self):
        connection = sqlite3.connect('Temperature.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY, sample_date TEXT UNIQUE, min_temp REAL, max_temp REAL, avg_temp REAL)")
        connection.commit()
        print("Database created successfully.")
        connection.close()
        
    def purge_data(self):
        connection = sqlite3.connect('Temperature.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM temperature')
        connection.commit()
        connection.close()

db_operations = DBOperations()
db_operations.initialize_db()
