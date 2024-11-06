
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, exc


# Database credentials from environment variables
DB_HOST = 'localhost'
DB_PORT=3306
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'task'
DATABASE_URL=DATABASE_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


def fetch_registration_data():
    connection = None  # Initialize connection as None for error handling
    try:
        # Establish a secure connection to the database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        
        if connection.is_connected():
            query = """
                SELECT acc.program AS Program, acc.email AS Email, crs.course_name AS Course_Name, tca.level AS Applying_Level, app.level AS Current_Level, crs.fee AS Fee_Details, app.status AS Application_Status FROM  TermCourseRegistrationApplication AS tca JOIN Application AS app ON tca.application_id = app.id JOIN Account AS acc ON app.account_id = acc.id JOIN Course AS crs ON tca.course_id = crs.id;
            """
            engine = create_engine(DATABASE_URL)
            # Execute query and fetch data
            df = pd.read_sql(query, engine)
            return df

    except Error as e:
        print("Error while connecting to the database or executing the query:", e)
        return None
    
    finally:
        # Close the database connection if it was established
        if connection and connection.is_connected():
            connection.close()
            #print("MySQL connection closed.")

# Fetch data and display the DataFrame
df = fetch_registration_data()
if df is not None:
    print(df.head())
