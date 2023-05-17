import csv
import os.path

from api_test.base_api_page import Base_Api_Page
from utilities.ReadProperties import configRead


class Test_Api(Base_Api_Page):

    def test_get_api_and_check_status_code(self):
        resp = self.get(configRead.ReadGetUrl())
        print("resp text", resp.text)
        code = self.check_status_code(resp, 200)
        assert code


    def test_response_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert "Michael" in python_dict['data'][0]['first_name']


    def test_value_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert python_dict['per_page'] == 6
        assert python_dict['total'] == 12


    def test_last_name_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert "Edwards" in python_dict['data'][4]['last_name']


    def test_page_value_in_python_dictionary(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        assert python_dict['total'] == 12

    def test_get_all_links(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        all_records = python_dict['data']
        for record in all_records:
            # print(record['avatar'])
            my_links = record['avatar']
            print(my_links)


    # def test_store_all_records_in_a_file(self):
    #     resp = self.get(configRead.ReadGetUrl())
    #     json_string = resp.text
    #     python_dict = self.convert_json_string_to_python_dictionary(json_string)
    #     all_records = python_dict['data']
    #     all_link =[]
    #     for record in all_records:
    #         my_links = record['avatar']
    #         all_link.append(my_links)
    #     print("&&&&&---->", all_link)
    #     with open('./../testData/LinksData.csv', 'w') as f:
    #         csv_writer = csv.writer(f)
    #         csv_writer.writerow(['Links']) #written in list else will get comma separated values
    #         for link in all_link:
    #             csv_writer.writerow([link])

    def test_store_all_records_in_a_file(self):
        resp = self.get(configRead.ReadGetUrl())
        json_string = resp.text
        python_dict = self.convert_json_string_to_python_dictionary(json_string)
        all_records = python_dict['data']
        all_first_name = []
        all_last_name = []
        all_email =[]
        all_link = []

        for record in all_records:
            first_name = record['first_name']
            last_name = record['last_name']
            email = record['email']
            my_links = record['avatar']
            all_link.append(my_links)
            all_first_name.append(first_name)
            all_last_name.append(last_name)
            all_email.append(email)
        path = os.path.abspath('./..//automation_framework//testData//LinksData.csv')
        with open(path, 'w', newline="") as f:
        # with open('./..//testData//LinksData.csv', 'w', newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['First_Name', 'Last_Name', 'Emails', 'Links'])  # written in list else will get comma separated values
            for i in range(len(all_first_name)):
                content = [all_first_name[i], all_last_name[i], all_email[i], all_link[i]]
                csv_writer.writerow(content)
















