from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" - incognito")
chromedriver_path = '/home/larri/Downloads/chromedriver'
def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)