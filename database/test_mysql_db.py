import pytest
import pandas as pd
from sqlalchemy import create_engine
from database.base_db_page import mysql_connect
import os

class Test_Mysql_Db(mysql_connect):

    def test_connect_db(self):
        connection = self.connect_using_mysql_connector()
        print("&&&&&&&&&&&&&&&&&&", connection)
        cursor = connection.cursor()
        print(cursor)
        return cursor

    def test_insert_google_maps_reviews_data_to_database1(self):
        my_conn = self.connect_using_sqlalchemy()
        path = os.path.abspath("reports//google_reviews.csv")
        print("&&&&",path)
        df = self.read_csv_using_pandas(path)
        print(df)
        self.insert_to_database_using_pandas(my_conn, 'replace', True, 'google_reviews', df)

    def test_insert_apis_into_database(self):
        my_conn = self.connect_using_sqlalchemy()
        path = os.path.abspath("testData//LinksData.csv")
        df = self.read_csv_using_pandas(path)
        print("my_csvdata------>>")
        print(df)
        self.insert_to_database_using_pandas(my_conn, 'replace', False, 'all_links', df)
















