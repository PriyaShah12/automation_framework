from selenium import webdriver
import pytest
from ui_test.pageObjects.login_page import Login
from utilities.ReadProperties import configRead
import time

class Test_001_login:

    def test_homepagetitle(self,use_fixture_before_all_methods):
        base_url,username, password, driver = use_fixture_before_all_methods
        act_title ="Your store. Login"
        if driver.title == act_title:
            assert True
        else:
            # driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            assert False


    def test_login(self, use_fixture_before_all_methods):
        base_url,username, password, driver = use_fixture_before_all_methods
        self.lp = Login(driver)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(6)
        actual_title = "Dashboard / nopCommerce administration"
        if driver.title == actual_title:
            assert True
        else:
            assert False



