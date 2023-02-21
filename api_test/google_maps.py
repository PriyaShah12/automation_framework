from bs4 import BeautifulSoup
from lxml import html
import requests

page = requests.get('https://www.google.com/maps/place/Mici+Asian+Bistro/@41.2777986,-73.2269953,17z/data=!3m1!5s0x89e809ab70fd9607:0x6910b2a93382aa0f!4m7!3m6!1s0x89e809ab6e3dd43f:0x1ffe3c983b90d799!8m2!3d41.2777986!4d-73.2269953!9m1!1b1')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
print(soup.title.string)

all_links_on_page = len(soup.findAll('a'))
print(f"There are {all_links_on_page} links in this page")


print("************")

rev = soup.find_all(
    "div", string=lambda text: "Ch")
print("%%%%%%%%%%")
print(len(rev))
for r in rev:
    print(r)
