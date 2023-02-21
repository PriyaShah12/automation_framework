from ui_test.pageObjects.login_page import Login
from ui_test.pageObjects.add_customer import AddCustomer
from utilities.ReadProperties import configRead
from configuration.test_data import search_customer
from ui_test.pageObjects.search_customer_page import searchcustomer
import pytest
import time

@pytest.mark.usefixtures("launch_url")
class Test_SearchCustomerByEmail_004:
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()


    def test_searchbyemail(self,init_driver):
        driver=init_driver

        self.lp=Login(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
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

