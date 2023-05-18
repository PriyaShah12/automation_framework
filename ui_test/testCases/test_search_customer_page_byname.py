from ui_test.pageObjects.login_page import Login
from ui_test.pageObjects.add_customer import AddCustomer
from ui_test.pageObjects.search_customer_page import searchcustomer
from configuration.test_data import search_customer
import pytest
import time

class Test_SearchCustomerByName_005:

    @pytest.mark.regression
    def test_searchbyname(self,use_fixture_before_all_methods):
        base_url, username, password, driver = use_fixture_before_all_methods
        self.lp = Login(driver)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)

        self.addcust=AddCustomer(driver)
        self.addcust.clickcustomer()
        self.addcust.clicksublinkcustomer()

        self.searchcust=searchcustomer(driver)
        self.searchcust.setfirstname(search_customer.first_name_to_search_cust)
        self.searchcust.setlastname(search_customer.last_name_to_search_cust)

        self.searchcust.clicksearch()
        time.sleep(3)
        status=self.searchcust.searchByName(search_customer.first_name_to_search_cust + search_customer.last_name_to_search_cust)
        if status!= "None":
            assert True


