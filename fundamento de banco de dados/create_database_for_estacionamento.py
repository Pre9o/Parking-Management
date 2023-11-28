import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"

class create_database_for_estacionamento():
    def __init__(self, host_name, user_name, user_password):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.define_database(host_name, user_name, user_password)
    
    def create_server_connection(self, host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
            
    def create_database(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def define_database(self, host_name, user_name, user_password):
        connection = self.create_server_connection(host_name, user_name, user_password)
        query = "CREATE DATABASE estacionamento"
        self.create_database(connection, query)
        connection.close()
        