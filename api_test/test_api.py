import csv
import time
import pytest
from api_test.base_api_page import Base_Api_Page
from utilities.ReadProperties import configRead
import pandas as pd


class Test_Api(Base_Api_Page):

    # @pytest.mark.skip
    def test_get_api_and_check_status_code(self):
        resp = self.get(configRead.ReadGetUrl())
        print("resp text", resp.text)
        code = self.check_status_code(resp, 200)
        assert code

    # @pytest.mark.skip
    def test_response_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert "Michael" in python_dict['data'][0]['first_name']

    # @pytest.mark.skip
    def test_value_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert python_dict['per_page'] == 6
        assert python_dict['total'] == 12

    # @pytest.mark.skip
    def test_last_name_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert "Edwards" in python_dict['data'][4]['last_name']

    # @pytest.mark.skip
    def test_page_value_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert python_dict['total'] == 12

    # @pytest.mark.skip
    def test_get_all_links(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        all_records = python_dict['data']
        for record in all_records:
            # print(record['avatar'])
            my_links = record['avatar']
            print(my_links)


    # @pytest.mark.skip
    def test_store_all_records_in_a_file(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        all_records = python_dict['data']
        all_link =[]
        for record in all_records:
            my_links = record['avatar']
            all_link.append(my_links)
        print("&&&&&---->", all_link)
        with open('./testData/LinksData.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Links']) #written in list else will get comma separated values
            for link in all_link:
                csv_writer.writerow([link])

















