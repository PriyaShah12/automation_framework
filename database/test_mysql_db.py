import pytest
import pandas as pd
from sqlalchemy import create_engine
from database.base_db_page import mysql_connect
import sys
import os


class Test_Mysql_Db(mysql_connect):

    @pytest.mark.skip
    def test_connect_db(self):
        connection = self.connect_using_mysql_connector()
        print("&&&&&&&&&&&&&&&&&&", connection)
        cursor = connection.cursor()
        print(cursor)
        # my_dict = {
        #     'class': ["four", 'five', 'six'],
        #     'Number': [4, 5, 5]
        # }
        # df = pd.DataFrame(data=my_dict)
        # print(df)
        # df.to_sql(con= connection,name='student', if_exists='replace', index=False)
        return cursor


    @pytest.mark.skip

    def test_insert_apis_into_database(self):
        # my_conn = self.connect_using_mysql_connector()
        my_conn = self.connect_using_sqlalchemy()
        path = os.path.abspath(r"./../testData//LinksData.csv")
        df = self.read_csv_using_pandas(path)

        # df = self.read_csv_using_pandas(r"./../testData//LinksData.csv")
        print("my_csvdata------>>")
        print(df)
        self.insert_to_database_using_pandas(my_conn, 'replace', False, 'all_links', df)

    @pytest.mark.skip
    def test_insert_google_maps_reviews_data_to_database(self):
        # my_conn = self.connect_using_mysql_connector()
        my_conn = self.connect_using_sqlalchemy()
        # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__)
        path = (r"./..//reports//google_reviews.csv")
        df = self.read_csv_using_pandas(path)
        print(df)
        self.insert_to_database_using_pandas(my_conn, 'replace', True, 'google_reviews', df )

    def test_insert_google_maps_reviews_data_to_database1(self):
        # my_conn = self.connect_using_mysql_connector()
        my_conn = self.connect_using_sqlalchemy()

        path = (r"./..//reports//google_reviews.csv")
        print("&&&&",path)
        # df = self.read_csv_using_pandas(path)
        # print(df)
        # self.insert_to_database_using_pandas(my_conn, 'replace', True, 'google_reviews', df)













