import sqlite3
from sqlite3 import Error
from datetime import datetime

class Logger:
    def write_log_to_system(self, message):
        print(f"Log to system: {message}")

class ErrorLogger(Logger):
    def __init__(self):
        self.create_table()  # Create the table when an instance is created

    def create_table(self):
        try:
            con = sqlite3.connect('sqldb.db', timeout=10)  # Set a timeout of 10 seconds
            con.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode
            sql = """
            CREATE TABLE IF NOT EXISTS ErrorLog (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Message TEXT
            );
            """
            con.execute(sql)
            con.commit()
        except sqlite3.Error as e:
            print(f"Database error during table creation: {e}")
        finally:
            if con:
                con.close()  # Ensure the connection is closed

    def write_log_to_file(self, message):
        try:
            with open('log.txt', 'a') as writer:
                writer.write(message + '\n')
                writer.flush()
        except Exception as e:
            print(f"Error occurred while writing to log file: {e}")

    def write_log_to_db(self, message):
        try:
            con = sqlite3.connect('sqldb.db', timeout=10)  # Set a timeout of 10 seconds
            con.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode
            sql = "INSERT INTO ErrorLog (Message) VALUES (?)"
            con.execute(sql, (message,))
            con.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if con:
                con.close()  # Ensure the connection is closed

# Main program block
try:
    a = int(input('Enter Value for No1: '))
    b = int(input('Enter Value for No2: '))
    result = a / b
    print(f"{a} / {b} = {result}")

except Exception as ex:
    el = ErrorLogger()
    message = f"""From OCP.py Program:
    Error: {ex}
    Error occurred while performing calculations.
    Please check the inputs.
    Date Time: {datetime.now()}
    """
    
    el.write_log_to_system(message)
    el.write_log_to_file(message)
    el.write_log_to_db(message)
    
    print(f"Error: {message}")
