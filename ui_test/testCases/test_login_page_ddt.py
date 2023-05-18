from ui_test.pageObjects.login_page import Login
from utilities import PathUtils
from utilities import ExcelUtils
import time
import pandas as pd


class Test_001_login:

    def test_login_ddt(self, use_fixture_before_all_methods):
        base_url,username, password, driver = use_fixture_before_all_methods
        self.lp = Login(driver)
        time.sleep(3)
        func_name = Test_001_login.test_login_ddt.__name__
        print(func_name)
        file = PathUtils.get_file(func_name)
        print("File Name-->", file)
        time.sleep(3)
        df = pd.read_excel(file)
        # print(df)
        report =[]
        for i in range(0, len(df)):
            self.lp = Login(driver)
            usrname, pswd, exp = df.iloc[i]['username'], df.iloc[i]['password'], df.iloc[i]['exp']
            print("username-->", usrname)
            print("password-->", pswd)
            print("exp-->", exp)
            self.lp.setUserName(usrname)
            self.lp.setPassword(pswd)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if exp == "pass":
                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('pass')
                elif exp == "fail":
                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('fail')
            elif act_title != exp_title:
                if exp == 'pass':
                    report.append('fail')
                    time.sleep(3)
                elif exp == 'fail':
                    report.append('pass')
                    time.sleep(3)
            if 'fail' not in report:
                time.sleep(2)
                assert True
            else:
                time.sleep(2)
                assert False

    def test_login_page_title_ddt(self,use_fixture_before_all_methods):
        base_url,username, password, driver = use_fixture_before_all_methods
        act_title = driver.title
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login_ddt_openpyxl(self,use_fixture_before_all_methods):
        base_url,username, password, driver = use_fixture_before_all_methods
        # self.lp= Login(driver)
        time.sleep(5)
        func_name = Test_001_login.test_login_ddt.__name__
        print(func_name)
        file = PathUtils.get_file(func_name)
        print("File Name-->", file)
        self.rows=ExcelUtils.getRowCount(file, "Sheet1")
        print("Number of rows:", self.rows)
        report=[]
        time.sleep(3)
        for r in range(2, self.rows+1):
            driver.get(base_url)
            self.lp = Login(driver)
            self.usrname = ExcelUtils.readData(file, 'Sheet1', r, 1)
            self.pswd = ExcelUtils.readData(file, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(file, 'Sheet1', r, 3)
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
                time.sleep(3)
                assert True
            else:
                time.sleep(3)
                assert False





