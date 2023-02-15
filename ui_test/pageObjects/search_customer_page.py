from selenium.webdriver.common.by import By
from ui_test.pageObjects.base_page import BasePage

class searchcustomer(BasePage):
    textbox_email_xpath="//input[@id='SearchEmail']"
    textbox_firstname_xpath="//input[@id='SearchFirstName']"
    textbox_lastname_xpath="//input[@id='SearchLastName']"
    button_search_xpath="//button[@id='search-customers']"
    tablegrid_xpath="//table[@id='customers-grid']"
    tablerows_xpath="//table[@id='customers-grid']//tbody/tr"
    tablecolumn_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def setemail(self, email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setfirstname(self, fname):
        self.driver.find_element(By.XPATH,self.textbox_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.XPATH,self.textbox_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()

    def getRowCount(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerows_xpath))

    def getColumnCount(self):
        return len(self.driver.find_elements(By.XPATH,self.tablecolumn_xpath))

    def searchByEmail(self, email):
        flag=False
        for r in range(1, self.getRowCount()+1):
            table=self.driver.find_element(By.XPATH, self.tablegrid_xpath)
            EmailId=table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[2]").text
            if EmailId == email:
                flag=True
                break
        return flag


    def searchByName(self, name):
        flag=False
        for r in range (1,self.getRowCount()+1):
            table=self.driver.find_element(By.XPATH,self.tablegrid_xpath)
            Name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]").text
            if Name==name:
                flag=True
                break
        return flag


