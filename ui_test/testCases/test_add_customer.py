from ui_test.pageObjects.login_page import Login
from utilities.ReadProperties import configRead
from ui_test.pageObjects.add_customer import AddCustomer
import pytest
import random
import string
import time
from selenium.webdriver.common.by import By
from configuration.test_data import add_customer

class Test_003_addcustomer:


    def test_addcustomer(self,use_fixture_before_all_methods):
        base_url, username, password, driver = use_fixture_before_all_methods
        self.lp = Login(driver)
        self.addcust = AddCustomer(driver)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()

        self.addcust.clickcustomer()
        self.addcust.clicksublinkcustomer()
        self.addcust.clickaddNew()

        self.email= random_generator()+"@gmail.com"
        self.addcust.enter_email(self.email)
        self.addcust.enter_password(add_customer.password)
        self.addcust.enter_first_name(add_customer.first_name)
        self.addcust.enter_last_name(add_customer.last_name)
        self.addcust.clicksetgender(add_customer.gender)
        self.addcust.enter_date_of_birth(add_customer.date_of_birth)
        self.addcust.enter_company_name(add_customer.company_name)
        self.addcust.click_tax_exempt()
        self.addcust.click_news_letter(add_customer.news_letter_name)
        # self.addcust.click_customer_role("Administrators")
        self.addcust.click_manager_of_vendor(add_customer.manager_of_vendor)
        self.addcust.click_save_button()
        self.msg=driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True
        else:
            assert False
        driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for r in range(size))





