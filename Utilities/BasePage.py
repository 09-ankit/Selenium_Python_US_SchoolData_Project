from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from Resources_Reader.ConfigReader import read_configs


class BasePage:


    def __init__(self):
        self.URL = read_configs("url")
        self.webdriver_path = Service(read_configs("WebDriverPath"))
        self.driver = webdriver.Chrome(service=self.webdriver_path)
        self.driver.get(self.URL)
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(10)



    def CloseBrowser(self):
        self.driver.close()


