from ui_test.pageObjects.login_page import Login
from ui_test.pageObjects.add_customer import AddCustomer
from configuration.test_data import search_customer
from ui_test.pageObjects.search_customer_page import searchcustomer
import time


class Test_SearchCustomerByEmail_004:

    def test_searchbyemail(self,use_fixture_before_all_methods):
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
        self.searchcust.setemail(search_customer.email_to_search_cust)
        self.searchcust.clicksearch()
        time.sleep(3)
        status=self.searchcust.searchByEmail(search_customer.email_to_search_cust)
        assert True==status
        driver.close()

