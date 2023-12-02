import sqlite3
import atexit

class DBCM:
    def __init__(self):
        """
        Initialize the DBCM class with the SQLite database file.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_file = "Temperature.db"
        self.connection = None
        self.cursor = None
        atexit.register(self.close_db)

    def close_db(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
    def __enter__(self):
        """
        Establish a SQLite database connection and return a cursor.

        Returns:
            cursor: A database cursor.
        """
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Commit changes, close the cursor, and close the SQLite database connection.

        Args:
            exc_type: The type of exception that occurred, if any.
            exc_value: The exception instance that occurred, if any.
            traceback: The traceback of the exception, if any.
        """
        if exc_type is None:  # Commit changes only if no exception occurred
            self.connection.commit()

        # Close the cursor and the SQLite database connection
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()

        # Raise the exception if any occurred
        return False  # Propagate the exception
