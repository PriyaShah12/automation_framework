from ui_test.pageObjects.login_page import Login
from ui_test.pageObjects.add_customer import AddCustomer
from utilities.ReadProperties import configRead
from ui_test.pageObjects.search_customer_page import searchcustomer
from configuration.test_data import search_customer
import pytest
import time

@pytest.mark.usefixtures("launch_url")
class Test_SearchCustomerByName_005:
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()

    @pytest.mark.regression
    def test_searchbyname(self,init_driver):
        self.driver=init_driver
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickcustomer()
        self.addcust.clicksublinkcustomer()

        self.searchcust=searchcustomer(self.driver)
        self.searchcust.setfirstname(search_customer.first_name_to_search_cust)
        self.searchcust.setlastname(search_customer.last_name_to_search_cust)

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
        self.searchcust.clicksearch()
        print("%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%5")

        time.sleep(3)
        status=self.searchcust.searchByName(search_customer.first_name_to_search_cust + search_customer.last_name_to_search_cust)
        print("Status----------->", status)
        time.sleep(3)
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

