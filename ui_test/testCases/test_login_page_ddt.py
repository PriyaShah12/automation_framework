import pytest
from ui_test.pageObjects.login_page import Login
from utilities.ReadProperties import configRead
from utilities import ExcelUtils
from utilities import PathUtils
import time


class Test_001_login:
    base_url=configRead.ReadUrl()
    path=".//TestData/DDT_testsheet.xlsx"

    @pytest.mark.skip
    def test_login_page_title_ddt(self,init_driver):
        driver = init_driver
        act_title = driver.title
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    @pytest.mark.skip(reason="Run Later")
    def test_login_ddt_11(self,init_driver):
        driver=init_driver
        # self.lp= Login(driver)
        time.sleep(5)
        self.rows=ExcelUtils.getRowCount(self.path, "Sheet1")
        print("Number of rows:", self.rows)
        report=[]
        time.sleep(3)
        for r in range(2, self.rows+1):
            driver.get(self.base_url)
            self.lp = Login(driver)
            self.usrname = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.pswd = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(3)
            self.lp.setUserName(self.usrname)
            self.lp.setPassword(self.pswd)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('pass')
                elif self.exp == "fail":

                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    report.append('fail')
                    time.sleep(3)
                elif self.exp == 'fail':
                    report.append('pass')
                    time.sleep(3)

            if 'fail' not in report:
                driver.close()
                time.sleep(3)
                assert True
            else:
                driver.close()
                time.sleep(3)
                assert False

    # @pytest.mark.skip(reason="Run Later")
    def test_login_ddt(self,  init_driver):
        driver=init_driver
        self.lp= Login(driver)
        time.sleep(3)
        func_name = Test_001_login.test_login_ddt.__name__
        file = PathUtils.get_file(func_name)
        time.sleep(3)
        self.rows=ExcelUtils.getRowCount(file, "Sheet1")
        print("Number of rows:", self.rows)
        report=[]
        time.sleep(3)
        for r in range(2, self.rows+1):
            driver = init_driver
            time.sleep(5)
            func_name = Test_001_login.test_login_ddt.__name__
            file = PathUtils.get_file(func_name)
            time.sleep(3)
            self.usrname = ExcelUtils.readData(file, 'Sheet1', r, 1)
            print(self.usrname)
            self.pswd = ExcelUtils.readData(file, 'Sheet1', r, 2)
            print(self.pswd)
            self.exp = ExcelUtils.readData(file, 'Sheet1', r, 3)
            print(self.exp)
            time.sleep(5)
            base_url = configRead.ReadUrl()
            driver.get(base_url)
            self.lp = Login(driver)
            time.sleep(3)
            self.lp.setUserName(self.usrname)
            self.lp.setPassword(self.pswd)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                time.sleep(3)
                if self.exp == "pass":
                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('pass')
                elif self.exp == "fail":

                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('fail')
            elif act_title != exp_title:
                time.sleep(3)
                if self.exp == 'pass':
                    report.append('fail')
                    time.sleep(3)
                elif self.exp == 'fail':
                    report.append('pass')
                    time.sleep(3)

            if 'fail' not in report:
                driver.close()
                time.sleep(3)
                assert True
            else:
                driver.close()
                time.sleep(3)
                assert False

















