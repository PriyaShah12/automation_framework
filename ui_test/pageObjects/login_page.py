import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ui_test.pageObjects.base_page import BasePage


class Login(BasePage):
    textbox_username_xpath= "//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_xpath="//a[contains(text(),'Logout')]"


    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
