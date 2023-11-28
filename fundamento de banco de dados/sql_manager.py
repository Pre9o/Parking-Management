import mysql.connector
from mysql.connector import Error
from datetime import datetime

host_name = "localhost"
user_name = "root"
user_password = "123456"
database_name = "estacionamento"

class sql_manager():
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = self.create_server_connection(host_name, user_name, user_password, database_name)
        self.cursor = self.connection.cursor()
        
    def create_server_connection(self, host_name, user_name, user_password, database_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection
    
    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    
    def execute_read_query(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
            
    def close_connection(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
            
    def insert_into_table(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Insert into table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def select_from_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
            
    def delete_from_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Delete from table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            
    def update_table(self, query):
        cursor = self.cursor
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Update table successfully")
        except Error as err:
            print(f"Error: '{err}'")
            