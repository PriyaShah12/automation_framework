import csv

import pytest
from ui_test.pageObjects.google_maps_page import Google_Maps
from utilities.ReadProperties import configRead
import time
from configuration.test_data import login_data
from bs4 import BeautifulSoup

@pytest.mark.usefixtures('launch_google_maps_url')
class Test_Google_Maps:

    def test_get_url(self,init_driver):
        driver = init_driver
        self.gp = Google_Maps(driver)
        self.gp.click_review()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup.prettify())
        csv_file = open("google_reviews.csv", "w")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name'  , 'Rating',   'Rating time',  'Review'])

        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:  # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Wait to load page
            time.sleep(3)
            for all_reviews in soup.find_all("div", class_ = 'jftiEf fontBodyMedium'):
                reviews = all_reviews.find('span', class_= 'wiI7pd')
                print("------------>>>", reviews.text)
                names = all_reviews.find('div', class_ = 'd4r55')
                print("==============.....>>>>", names.text)
                ratings = all_reviews.find('span', class_ = 'kvMYJc')['aria-label']
                print("$$$$$$$$$$$$$---->", ratings)
                rating_time = all_reviews.find("div", class_='DU9Pgb')
                print("%%%%%%%--->", rating_time.text)
                csv_writer.writerow([names.text, ratings, rating_time.text, reviews.text ])

            self.gp.page_scroll()
            print()
            new_height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(3)
            if new_height == last_height:
                break
            last_height = new_height
            time.sleep(3)
        csv_file.close()










