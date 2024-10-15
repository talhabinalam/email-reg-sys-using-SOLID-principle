import sqlite3
from sqlite3 import Error
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Users:
    def __init__(self):
        # Create the Users table if it doesn't exist
        self.create_table()

    def create_table(self):
        try:
            con = sqlite3.connect('sqldb.db')
            cursor = con.cursor()
            # Create table with username, password, and email fields
            cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL,
                                email TEXT NOT NULL
                              );''')
            con.commit()
            con.close()
        except Error as e:
            logging.error(f"Error occurred while creating Users table: {e}")
            print(f"Error occurred while creating Users table: {e}")

    def register_user(self, uname, pwd, email):
        try:
            con = sqlite3.connect('sqldb.db')
            sql = "INSERT INTO Users (username, password, email) VALUES (?, ?, ?)"
            con.execute(sql, (uname, pwd, email))
            con.commit()
            con.close()
            print(f"User registered with {uname} and {email}")
        except Error as e:
            logging.error(f"Error occurred while registering user: {e}")
            print(f"Error occurred while registering user: {e}")


class Logger:
    def system_log(self, message):
        # Use logging.error instead of syslog
        logging.error(message)


import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def sent_email(self, to_email, msg_content):
        try:
            with open('credentials.json') as f:
                data = json.load(f)

            smtp = 'smtp.gmail.com'
            port = 465
            sender_email = data['from_user']
            password = data['password']

            context = ssl.create_default_context()
            message = MIMEMultipart("alternative")

            # Corrected "Form" to "From"
            message['From'] = sender_email
            message['To'] = to_email
            message['Subject'] = "User Registration"

            # Fixed f-string and content formatting
            msg_content = f'''Hello, <br/><b>Message from Talha Academy: </b><br/>
                            {msg_content} <br/>
                            All The Best <br/>Best Wishes, <br />TechnoAcademy, Support Team.'''

            part = MIMEText(msg_content, 'html')
            message.attach(part)

            with smtplib.SMTP_SSL(smtp, port, context=context) as server:
                server.login(sender_email, password)
                # Corrected message.string() to as_string()
                server.sendmail(sender_email, to_email, message.as_string())

            print(f"Email sent to {to_email}")

        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            print(f"Failed to send email: {e}")


class UserRegistration:
    def register_user(self, uname, pwd, email):
        try:
            # Register user in the database
            Users().register_user(uname, pwd, email)
            # Send confirmation email
            Email().sent_email(email, "You have successfully registered!")
            print("User registered and email sent.")
        except Exception as e:
            # Log any errors using logging module
            Logger().system_log(f"Error while registering: {str(e)}")
            print(f"Error: {str(e)}")


# Example usage:
r = UserRegistration()
r.register_user('talha', 'example123', 'mdtalhabinalam@outlook.com')
