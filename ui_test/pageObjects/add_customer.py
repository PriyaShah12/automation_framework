import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from ui_test.pageObjects.base_page import BasePage

class AddCustomer(BasePage):
    menusearchicon_xpath="//i[@class='fa fa-bars']"
    txtbox_email_xpath="//input[@id='Email']"
    txtbox_password_xpath="//input[@id='Password']"
    txtbox_firstname_xpath="//input[@id='FirstName']"
    txtbox_lastname_xpath="//input[@id='LastName']"
    radiobutton_male_xpath="//input[@id='Gender_Male']"
    radiobutton_female_xpath="//input[@id='Gender_Female']"
    txtbox_dateOfBirth_xpath="//input[@id='DateOfBirth']"
    txtbox_companyname_xpath="//input[@id='Company']"
    checkbox_taxexempt_xpath="//input[@id='IsTaxExempt']"
    link_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    sublink_customer_xpath="//a[@href='/Admin/Customer/List']"
    addnew_button_xpath="//a[@class='btn btn-primary']"
    txtbox_newsletter_xpath="//div[@class='col-md-9']//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_yourstorename_xpath="//li[contains(text(),'Your store name')]"
    listitem_testscore2_xpath="//li[contains(text(),'Test store 2')]"
    txtbox_customerroles_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    listitem_administrator_xpath="//li[contains(text(),'Administrators')]"
    listitem_moderator_xpath="//li[contains(text(),'Forum Moderators')]"
    listitem_guest_xpath="//li[contains(text(),'Guests')]"
    listitem_registered_xpath="//li[contains(text(),'Registered')]"
    cut_registered_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[2]"
    listitem_vendors_xpath="//li[contains(text(),'Vendors')]"
    drpdown_managerOfVendor_xpath="//select[@name='VendorId']"
    drpdown_vendor1_xpath="//select[@name='VendorId']//[contains(text(),'Vendor 1')]"
    drpdown_vendor2_xpath="//select[@name='VendorId']//[contains(text(),'Vendor 2')]"
    checkbox_active_xpath="//input[@id='Active']"
    textbox_admincomment_xpath="//textarea[@id='AdminComment']"
    button_save_xpath="//button[@name='save'][@type='submit']"


    def menusearch(self):
        self.driver.find_element(By.XPATH,self.menusearchicon_xpath).click()

    def clickcustomer(self):
        self.driver.find_element(By.XPATH,self.link_customer_xpath).click()

    def clicksublinkcustomer(self):
        self.driver.find_element(By.XPATH,self.sublink_customer_xpath).click()

    def clickaddNew(self):
        self.driver.find_element(By.XPATH,self.addnew_button_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.txtbox_password_xpath).send_keys(password)

    def enter_first_name(self, firstname):
        self.driver.find_element(By.XPATH,self.txtbox_firstname_xpath).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.XPATH,self.txtbox_lastname_xpath).send_keys(lastname)

    def clicksetgender(self, gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.radiobutton_male_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.radiobutton_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.radiobutton_male_xpath).click()


    def enter_date_of_birth(self, dob):
        self.driver.find_element(By.XPATH,self.txtbox_dateOfBirth_xpath).send_keys(dob)

    def enter_company_name(self, companyname):
        self.driver.find_element(By.XPATH,self.txtbox_companyname_xpath).send_keys(companyname)

    def click_tax_exempt(self):
        self.driver.find_element(By.XPATH,self.checkbox_taxexempt_xpath).click()

    def click_news_letter(self, role):
        self.driver.find_element(By.XPATH,self.txtbox_newsletter_xpath).click()
        time.sleep(2)
        if role=="Your store name":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_yourstorename_xpath)
        elif role=="Test store 2":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_testscore2_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def click_customer_role(self, role):
        self.driver.find_element(By.XPATH,self.txtbox_customerroles_xpath).click()
        time.sleep(2)
        if role=="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_registered_xpath)
        elif role=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_vendors_xpath)
        elif role=="Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_administrator_xpath)
        elif role=="Forum Moderators":
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_moderator_xpath)
        elif role=="Guests":
            self.driver.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[2]").click()
            self.listitem=self.driver.find_element(By.XPATH,self.listitem_guest_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_guest_xpath)
        time.sleep(2)
        # self.listitem.click()
        self.driver.execute_script("arguments[0],click();", self.listitem)

    def click_manager_of_vendor(self, value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpdown_managerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def click_save_button(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()















