# 6. Build a Flask app that allows users to upload files and display them on the website. 

from flask import Flask
import requests
from bs4 import BeautifulSoup
import mysql.connector
import time

url='https://tcvvip5.com/#/home/AllLotteryGames/WinTrx?id=4'
 
response =requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# MySQL database configuration
db_config = {
    'host': 'your_mysql_host',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'your_mysql_database'
}

# Website authentication credentials (if required)
auth_data = {
    'username': 'your_username',
    'password': 'your_password'
}

# Function to authenticate with the website
def authenticate(session):
    # Implement authentication logic here
    # Use session.post() or other methods to perform login

# Function to retrieve and store data
def retrieve_and_store_data():
    # Create a persistent session
    with requests.Session() as session:
        # Authenticate with the website (if required)
        authenticate(session)

        # Make a request to the website
        response = session.get('https://example.com')

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the soup
        data_to_store = soup.find('div', {'class': 'example-class'}).text

        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
        cursor.execute(insert_query, (data_to_store, 'additional_data'))

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

# Run the script in a loop to retrieve and store data every 5 minutes
while True:
    retrieve_and_store_data()
    time.sleep(300)  # Sleep for 5 minutes
