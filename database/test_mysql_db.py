import pytest
import pandas as pd
from database.base_db_page import mysql_connect


class Test_Mysql_Db(mysql_connect):

    # @pytest.mark.skip
    def test_connect_db(self):
        connection = self.connect()
        print("&&&&&&&&&&&&&&&&&&", connection)
        cursor = connection.cursor()
        print(cursor)
        path= "./testData/LinksData.csv"
        data= pd.read_csv(path, delim_whitespace=True, header=0,index_col=0)
        df = pd.DataFrame(columns=['links'] )
        print("*****", df)
        # df.to_sql(con=connection,if_exists='append',index=False, name=)



    # def test_insert_data_after_creating_table(self, mynewlinks):
    #     self.create_table(mynewlinks)







