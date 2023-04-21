import mysql.connector
import pandas as pd
from utilities.ReadProperties import configRead
from mysql.connector import MySQLConnection, Error
import json
from abc import ABC, abstractmethod
from sqlalchemy import create_engine, text
import sqlalchemy





class Database_Class(ABC):
    @abstractmethod
    def connect_using_mysql_connector(self):
        pass

    @abstractmethod
    def connect_using_sqlalchemy(self):
        pass

    @abstractmethod
    def read_csv_using_pandas(self, file_path, column_name, header_value, encoding='cp1252', sep=","):
        pass

    @abstractmethod
    def insert_to_database_using_pandas(self, dtbase_connection, ifexists, indexvalue, tablename, df):
        pass

    @abstractmethod
    def read_from_database_using_pandas(self, dtbase_connection, query):
        pass

    @abstractmethod
    def execute_a_query(self, query_to_execute, db_connection):
        pass

    @abstractmethod
    def execute_multiple_queries(self, queries_to_execute, value, db_connection):
        pass

    @abstractmethod
    def fetch_all_records(self, query, db_connection):
        pass

    @abstractmethod
    def fetch_only_one_record(self, query, db_connection):
        pass

class mysql_connect(Database_Class):
    def connect_using_mysql_connector(self):
        try:
            db_config = configRead.Read_DB_Config()
            conn = None
            print("Connecting to MySQL database...")
            conn = MySQLConnection(**db_config)
            if conn.is_connected():
                db_Info = conn.get_server_info()
                print("Connected to MySQL Server version:--> ", db_Info)
                print("Connection established with--->", conn)
                print(conn)
                return conn
        except Error as e:
            print("Error while connecting to MySQL", e)

    def connect_using_sqlalchemy(self):
        # my_conn = create_engine("mysql+pymysql://root:root@localhost:3306/testdb")
        my_conn = create_engine(f"mysql+pymysql://root:root@localhost:3306/testdb", echo=True, future=True)
        return my_conn


    def read_csv_using_pandas(self, file_path, column_name, header_value, encoding='cp1252', sep=","): #column_name should be list of values inside tuple
        df = pd.read_csv(file_path, names=column_name, header=header_value, encoding= encoding, sep=sep)
        return df

    def insert_to_database_using_pandas(self,dtbase_connection, ifexists, indexvalue, tablename, df):
        df.to_sql(con=dtbase_connection, if_exists=ifexists, index=indexvalue, name=tablename)
        df.to_sql()
        # df.to_sql(con=dtbase_connection, if_exists=ifexists, index=indexvalue, name=tablename)



    def read_from_database_using_pandas(self, dtbase_connection,my_query):
        df = pd.read_sql(dtbase_connection,my_query)
        return df

    def create_table(self, table_name):
        db_conn = self.connect_using_mysql_connector()
        cursor = db_conn.cursor()
        cursor.execute(f'drop table if exists {table_name}(num int )')
        cursor.execute(f"Create table {table_name}((num int )")
        db_conn.commit()


    def execute_a_query(self, query_to_execute, db_connection):
        connection = db_connection
        cursor = connection.cursor()
        # global connection timeout arguments
        '''global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)'''
        try:
            cursor.execute(query_to_execute)
            connection.commit()
            print("Query executed successfully********")
            print(cursor.rowcount, "rows printed")
        except:
            connection.rollback()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def execute_multiple_queries(self, queries_to_execute, value, db_connection):
        connection = db_connection
        cursor = connection.cursor()
        try:
            result_iterator = cursor.execute(queries_to_execute, value) #value is list of tuples
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows")
                print("Queries executed successfully********")
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
        print(cursor.rowcount, "rows printed")


    def fetch_all_records(self, query, db_connection):
        connection = db_connection
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            fetch_result = cursor.fetchall()
            print(json.dumps(fetch_result, indent=4))
            all_records = []
            for record in fetch_result:
                if record!= None:
                    all_records.append(record)
            print(all_records)
            return all_records
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()

    def fetch_only_one_record(self, query, db_connection):
        connection = db_connection
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        try:
            fetch_result = cursor.fetchone()
            print("Json Format:-->", json.dumps(fetch_result, indent=4))
        except mysql.connector.Error as error:
            print("Error while reading from MYSQL : ", error)
        finally:
            cursor.close()



