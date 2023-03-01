import pytest
import pandas as pd
from sqlalchemy import create_engine
from database.base_db_page import mysql_connect


class Test_Mysql_Db(mysql_connect):

    @pytest.mark.skip
    def test_connect_db(self):
        connection = self.connect_using_mysql_connector()
        print("&&&&&&&&&&&&&&&&&&", connection)
        cursor = connection.cursor()
        print(cursor)
        my_dict = {
            'class': ["four", 'five', 'six'],
            'Number': [4, 5, 5]
        }
        df = pd.DataFrame(data=my_dict)
        print(df)
        df.to_sql(con= connection,name='student', if_exists='replace', index=False)


    @pytest.mark.skip
    def test_insert_apis_into_database(self):
        # my_conn = self.connect_using_mysql_connector()
        my_conn = self.connect_using_sqlalchemy()
        df = self.read_csv_using_pandas(r".//testData//LinksData.csv", ['Links'], None)
        print("my_csvdata------>>", df)
        self.insert_to_database_using_pandas(my_conn, 'replace', True, 'all_links', df)


    def test_insert_google_maps_reviews_data_to_database(self):
        my_conn = self.connect_using_mysql_connector()
        # my_conn = self.connect_using_sqlalchemy()
        path = (r".//reports//google_reviews.csv")
        colmn_nme = ['Name', 'Rating', 'Rating time', 'Review']
        df = self.read_csv_using_pandas(path,colmn_nme, None)
        self.insert_to_database_using_pandas(my_conn, 'replace', False, 'google_reviews', 'testdb', df )
        query = "select * from all_links"
        df1 = pd.read_sql(query, my_conn)
        print("****", df1)

















