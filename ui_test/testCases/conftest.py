from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from utilities.ReadProperties import configRead
import time

# @pytest.fixture(scope="class", autouse=True)
@pytest.fixture(autouse=True) #if we dont provide any scope then by default it is for all functions/methods whereever method name is passed as paramter
def init_driver(browser = "Chrome"):
    # global driver
    if browser == 'Chrome':
        s= Service(executable_path="C:\\Priya_Dev\\sourcecode\\NopCommerce\\drivers\\chromedriver.exe")
        # s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == 'Firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser == "Edge":
        s = Service(EdgeChromiumDriverManager().install())
        driver= webdriver.Ie(service=s)
    elif browser == "IE":
        s = Service(IEDriverManager().install())
        driver = webdriver.Chrome(service=s)
    else:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()  #init_driver method will hold driver as its value and can be used by anymethod parameter in any file.

#
# @pytest.fixture #(autouse=True)  #if scope is not given then by default is function scope.
# def launch_url(init_driver):
#     base_url = configRead.ReadUrl()
#     driver = init_driver
#     driver.get(base_url)
#     driver.maximize_window()

# @pytest.fixture
# def launch_google_maps_url(init_driver):
#     base_url = configRead.ReadGoogleUrl()
#     driver = init_driver
#     driver.get(base_url)
#     driver.maximize_window()
#     time.sleep(3)

@pytest.fixture(scope='function', autouse=False)
def launch_google_maps_url(init_driver):
    base_url = configRead.ReadGoogleUrl()
    driver = init_driver
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(3)
    return driver

@pytest.fixture(scope='function', autouse=False)
def use_fixture_before_all_methods(init_driver):
    base_url = configRead.ReadUrl()
    username = configRead.ReadUsername()
    password = configRead.Readpassword()
    driver = init_driver
    driver.get(base_url)
    driver.maximize_window()
    return base_url, username, password, driver



