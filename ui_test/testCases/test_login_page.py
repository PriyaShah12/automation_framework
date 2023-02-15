import pytest
from ui_test.pageObjects.login_page import Login
from utilities.ReadProperties import configRead
import time
from configuration.test_data import login_data


class Test_Login:

    def test_login_page_title(self,init_driver):
        driver = init_driver
        # driver.get(configRead.ReadUrl())
        # driver.maximize_window()
        act_title=driver.title
        if act_title=="Your store. Login":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    # @pytest.mark.skip
    def test_login(self,init_driver):
        driver = init_driver
        driver.get(configRead.ReadUrl())
        driver.maximize_window()
        self.lp = Login(driver)
        self.lp.setUserName(configRead.ReadUsername())
        self.lp.setPassword(configRead.Readpassword())
        self.lp.clickLogin()
        time.sleep(6)

        act_title = driver.title
        if act_title == login_data.title:
            assert True
            driver.close()
        else:
           assert False


