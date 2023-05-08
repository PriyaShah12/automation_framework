# from bs4 import BeautifulSoup
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ui_test.pageObjects.base_page import BasePage


class Google_Maps(BasePage):

    review_rating_xpath = (By.XPATH, "//div[@class='LRkQ2']//div[contains(text(),'Reviews')]")
    all_reviews_text_xpath = (By.XPATH, "//div[starts-with(@id, 'Ch')]//span[2]")
    more_button_in_reviews = (By.XPATH, "//button[@class='w8nwRe kyuRq']")

    def click_review(self):
        print("***********************")
        ele = self.wait_until_an_element_present(self.review_rating_xpath)
        ele.click()

    def capture_all_reviews(self):
        all_reviews = self.wait_until_all_elements_present(self.all_reviews_text_xpath)
        for review in all_reviews:
            self.page_scroll()
            print(review.text)

    def click_more_text(self):
        ele = self.wait_until_an_element_present(self.more_button_in_reviews)
        ele.click()







