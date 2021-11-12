from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        self.service_chrome = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service_chrome)
        print('init Browser')

    def wait_load_page(self, by_element, search_element):
        """ ждем загрузку страницы """
        timeout = 1

        try:
            element_present = expected_conditions.presence_of_element_located((by_element, search_element))
            WebDriverWait(self.browser, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")
